import datetime

from django.db import models
from django.utils import timezone

class DecisionGroup(models.Model):
    scenario_text = models.CharField(max_length=400)

    def __str__(self):
        return self.scenario_text

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
    ('A', 'Average Worker'),
    ('D', 'Doctor')
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A',
    )

    #def __str__(self):
    #    return self.description

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