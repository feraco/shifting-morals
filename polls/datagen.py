from django.core.management.base import BaseCommand
from models import *

d = DecisionGroup(scenario_title="Test", scenario_description="Testing stuff")

d.save()