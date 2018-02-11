import datetime

from django.db import models
from django.utils import timezone

class DecisionGroup(models.Model):
    scenario_text = models.CharField(max_length=200)

    def __str__(self):
        return self.scenario_text

class Decision(models.Model):
    decision_set = models.ForeignKey(DecisionGroup, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description

class Person(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    age = models.IntegerField(default=1)
    in_car = models.BooleanField(default=False)
    following_law = models.BooleanField(default=True)

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
