import datetime

from django.core.cache import cache
from django.db import models
from django.utils import timezone

class DecisionGroup(models.Model):
    scenario_title = models.CharField(max_length=400)
    scenario_description = models.CharField(max_length=400, default=None)

    TYPES = (
    ('I', 'Individual'),
    ('L', 'Large'),
    )

    scenario_type = models.CharField(
        max_length=1,
        choices=TYPES,
        default='I',
    )

    def __str__(self):
        return self.scenario_title


class Decision(models.Model):
    decision_group = models.ForeignKey(DecisionGroup, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description


class Person(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, default=None)
    #description = models.CharField(max_length=400)
    #prob = models.ManyToManyField(Probability, through='Decision') see Probability class below

    PROB_CHOICES = (
    ('VL', 'Very low'),
    ('LW', 'Low'),
    ('MD', 'Medium'),
    ('HI', 'High'),
    ('VH', 'Very high'),
    )

    probability = models.CharField(
        max_length=2,
        choices=PROB_CHOICES,
        default='MD',
    )

    AGE_CHOICES = (
    ('C', 'Child'),
    ('A', 'Adult'),
    ('O', 'Old')
    )

    age = models.CharField(
        max_length=1,
        choices=AGE_CHOICES,
        default='A',
    )

    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'NA')
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='N',
    )

    STATUS_CHOICES = (
    ('C', 'Criminal'),
    ('A', 'Average'),  # Average worker
    ('D', 'Doctor')
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A',
    )

    #def __str__(self):
    #    return self.description

class Outcome(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, default=None)
    outcome_description = models.CharField(max_length=400)

    # Range for possible deaths
    min_value = models.PositiveIntegerField(default=0)
    max_value = models.PositiveIntegerField(default=0)

    # Must satisfy min_value < predicted_num_deaths < max_value
    predicted_num_deaths = models.IntegerField(default=0)

    CONFIDENCE_CHOICES = (
    ('LW', 'Low'),
    ('MD', 'Medium'),
    ('HI', 'High'),
    )

    # Confidence in predicted number of deaths
    confidence = models.CharField(
        max_length=2,
        choices=CONFIDENCE_CHOICES,
        default='MD',
    )

    # Likelihood that this outcome occurs -- must be number between 0 and 100
    # Set of outcomes for a decision should not have a culmulative outcome greater
    # than 100.
    # TODO: Add checks for > 100 outcome sum

    likelihood = models.PositiveIntegerField(default=0)


# From https://steelkiwi.com/blog/practical-application-singleton-design-pattern/
# Copyright © 2017 SteelKiwi, http://steelkiwi.com
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

class Statistics(SingletonModel):
    total_decisions = models.PositiveIntegerField(default=0)
    kill_count = models.PositiveIntegerField(default=0)
    male_kc = models.PositiveIntegerField(default=0)
    female_kc = models.PositiveIntegerField(default=0)
    group_kill_count = models.PositiveIntegerField(default=0)
    lives_saved = models.PositiveIntegerField(default=0)

    # Total -- range from - # decisions to + # decisions
    confidence_total = models.FloatField(default=0.0)
    status_total = models.FloatField(default=0.0)
    age_total = models.FloatField(default=0.0)

    # TODO: Change to char fields that say 'most people prefer this' etc,
    # and add logic for assigning the field in views.py

    CONFIDENCE_PREF = (
    ('LW', 'Most people prefer high risk situations.'),
    ('MD', 'Most people prefer medium risk situations.'),
    ('HI', 'Most people prefer low risk situations.'),
    )

    confidence_preference = models.CharField(
        max_length=2,
        choices=CONFIDENCE_PREF,
        default='MD',
    )

    STATUS_PREF = (
    ('C', 'Most people prefer criminals over doctors.'),
    ('A', "Most people don't have a preference for social status."),
    ('D', 'Most people prefer doctors over criminals.')
    )

    status_preference = models.CharField(
        max_length=2,
        choices=STATUS_PREF,
        default='A',
    )

    AGE_PREF = (
    ('C', 'Children are valued the most by the majority of people.'),
    ('A', 'Adults are valued the most by the majority of people.'),
    ('O', 'The eldery are valued the most by the majority of people.')
    )

    age_preference = models.CharField(
        max_length=2,
        choices=AGE_PREF,
        default='A',
    )

    # Helper fields for preferences
    group_decisions = models.PositiveIntegerField(default=0)
    individual_decisions = models.PositiveIntegerField(default=0)
    status_decisions = models.PositiveIntegerField(default=0)


# Not viable because no easy way to access on per person basis in templates
'''class Probability(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, default=None)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=None)

    PROB_CHOICES = (
    ('VL', 'Very low'),
    ('LW', 'Low'),
    ('MD', 'Medium'),
    ('HI', 'High'),
    ('VH', 'Very high'),
    )

    probability = models.CharField(
        max_length=2,
        choices=PROB_CHOICES,
        default='MD',
    ) '''