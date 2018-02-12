from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import *

import random


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

        if 'kill_count' not in request.session:
            request.session["kill_count"] = 0

        if 'male_kc' not in request.session:
            request.session["male_kc"] = 0

        if 'female_kc' not in request.session:
            request.session["female_kc"] = 0

        if 'passenger_kc' not in request.session:
            request.session["passenger_kc"] = 0

        if 'non_passenger_kc' not in request.session:
            request.session["non_passenger_kc"] = 0

        if 'age' not in request.session:
            request.session["age"] = []

        if 'avg_age' not in request.session:
            request.session["avg_age"] = 0

        request.session["killed_bool"] = False
        request.session["killed"] = 0

        prob_dict = {
            'VL': range(0,20),
            'LW': range(20,40),
            'MD': range(40,60),
            'HI': range(60,80),
            'VH': range(80,100)
        }

        for person in persons:
            if random.choice(prob_dict[person.probability])/100.0 < random.random():
                request.session["killed"] += 1
                request.session["kill_count"] += 1
                request.session["killed_bool"] = True
                request.session["age"].append(person.age)
                if person.gender == 'M':
                    request.session["male_kc"] += 1
                elif person.gender == 'F':
                    request.session["female_kc"] += 1
                if person.in_car:
                    request.session["passenger_kc"] += 1
                else:
                    request.session["non_passenger_kc"] += 1

        if len(request.session["age"]) != 0:
            request.session["avg_age"] = sum(request.session["age"])/len(request.session["age"])
        else:
            request.session["avg_age"] = 0

        selected_decision.save()
        return HttpResponseRedirect(reverse('polls:results', args=(decision_group.id,)))

