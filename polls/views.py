from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from chartjs.views.lines import BaseLineChartView
from chartjs.colors import next_color, COLORS

from .models import *

from random import choice, shuffle, randint, random


class DecisionView(generic.ListView):
    template_name = 'polls/decision.html'
    context_object_name = 'decisions_list'

    def get_queryset(self):
        return DecisionGroup.objects.values()

class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'

class AboutView(generic.TemplateView):
    template_name = 'polls/about.html'

class ContactView(generic.TemplateView):
    template_name = 'polls/contact.html'

class StatsView(generic.TemplateView):
    template_name = 'polls/stats.html'

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'

    context_object_name = 'decision_group'
    queryset = DecisionGroup.objects.all()

class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'

    context_object_name = 'decision_group'
    queryset = DecisionGroup.objects.all()


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return self.request.session["decisions_range"]  # range(self.request.session["num_decisions"])

    def get_providers(self):
        return ["Total Kills", "Male kills", "Female Kills"]

    def get_data(self):
        return [
            self.request.session["kill_list"], 
            self.request.session["male_kill_list"], 
            self.request.session["female_kill_list"]
        ]

    def get_colors(self):
        """Return a new shuffle list of color so we change the color
        each time."""
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)

    # Edited from the repo for django-chart js
    # https://github.com/peopledoc/django-chartjs/blob/master/chartjs/views/lines.py
    def get_datasets(self):
        datasets = []
        color_generator = self.get_colors()
        data = self.get_data()
        providers = self.get_providers()
        num = len(providers)
        for i, entry in enumerate(data):
            color = tuple(next(color_generator))
            #color = (0, 128, 0) # (122, 159, 191) for blue? Not sure which is better
            dataset = {'backgroundColor': "rgba(%d, %d, %d, 0.5)" % color,
                       'borderColor': "rgba(%d, %d, %d, 1)" % color,
                       'pointBackgroundColor': "rgba(%d, %d, %d, 1)" % color,
                       'pointBorderColor': "#fff",
                       'data': entry}
            if i < num:
                dataset['label'] = providers[i]  # series labels for Chart.js
                dataset['name'] = providers[i]  # HighCharts may need this
            datasets.append(dataset)
        return datasets

def vote(request, decision_group_id):
    decision_group = get_object_or_404(DecisionGroup, pk=decision_group_id)
    try:
        selected_decision = decision_group.decision_set.get(pk=request.POST['decision'])
        persons = selected_decision.person_set.all()
    except (KeyError, Decision.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'decision_group': decision_group,
            'error_message': "You didn't select a decision.",
        })
    else:
        selected_decision.votes += 1

        # Check if session variables exist

        if 'kill_count' not in request.session:
            request.session["kill_count"] = 0

        if 'male_kc' not in request.session:
            request.session["male_kc"] = 0

        if 'female_kc' not in request.session:
            request.session["female_kc"] = 0

        if 'age' not in request.session:
            request.session["age"] = []

        if 'status' not in request.session:
            request.session["status"] = 0.0

        if 'sum_status' not in request.session:
            request.session["sum_status"] = 0

        if 'status_percent' not in request.session:
            request.session["status_percent"] = 0.0

        if 'num_decisions' not in request.session:
            request.session["num_decisions"] = 0

        if 'decisions_range' not in request.session:
            request.session["decisions_range"] = []

        if 'kill_list' not in request.session:
            request.session["kill_list"] = []

        if 'male_kill_list' not in request.session:
            request.session["male_kill_list"] = []

        if 'female_kill_list' not in request.session:
            request.session["female_kill_list"] = []

        # Set variables that  need to be set each decision

        request.session["num_decisions"] += 1

        request.session["killed_bool"] = False  # If you kill any this decision
        request.session["killed"] = 0  # Refers to the number killed in this decision

        # Dicts for variables

        prob_dict = {
            'VL': range(0,20),
            'LW': range(20,40),
            'MD': range(40,60),
            'HI': range(60,80),
            'VH': range(80,100)
        }

        age_dict = {
            'C': 'Child',
            'A': 'Adult',
            'O': 'Old'
        }

        status_dict = {
            'C': 'Criminal',
            'A': 'Average Worker',
            'D': 'Doctor'
        }

        # Core logic for person deaths (prob is inverse because of ranges -- see the dict above)

        for person in persons:
            if (1.0 - choice(prob_dict[person.probability])/100.0) < random():
                request.session["killed"] += 1
                request.session["kill_count"] += 1
                request.session["killed_bool"] = True
                request.session["age"].append(person.age)
                if person.status == 'D':
                    request.session["status"] -= 1.0
                    request.session["sum_status"] += 1
                elif person.status == 'C':
                    request.session["status"] += 1.0
                    request.session["sum_status"] += 1

                if person.gender == 'M':
                    request.session["male_kc"] += 1
                elif person.gender == 'F':
                    request.session["female_kc"] += 1

        # Post processing of deaths and other factors

        if request.session["sum_status"] != 0:
            request.session["status_percent"] = request.session["status"]/request.session["sum_status"]
        else:
            request.session["status_percent"] = 0

        if request.session["status_percent"] < 0:
            request.session["social_preference"] = "You have a {:.2f}% preference for criminals over doctors.".format(abs(request.session["status_percent"])*100.0)
        elif request.session["status_percent"] > 0:
            request.session["social_preference"] = "You have a {:.2f}% preference for doctors over criminals.".format(abs(request.session["status_percent"])*100.0)
        else:
            request.session["social_preference"] = "You have no preference for doctors vs. criminals."

        if request.session["age"]:
            request.session["most_killed_age"] = age_dict[max(set(request.session["age"]), key=request.session["age"].count)]

        # TODO: Remove decisions range, replace with range(num_decisions)
        request.session["decisions_range"].append(request.session["num_decisions"])
        request.session["kill_list"].append(request.session["kill_count"])
        request.session["male_kill_list"].append(request.session["male_kc"])
        request.session["female_kill_list"].append(request.session["female_kc"])

        # Sanity checks
        #request.session["test"] = request.session["decisions_range"]
        #request.session["test2"] = request.session["kill_count"]


        # Save to db and return the http response redirect to results page

        selected_decision.save()
        return HttpResponseRedirect(reverse('polls:results', args=(decision_group.id,)))
