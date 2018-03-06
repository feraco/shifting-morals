from django.core.management.base import BaseCommand
from polls.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Run this command to generate data for the database. No args necessary.'

    def _create_scenarios(self):

        ''' Robotic cop Scenario '''

        self.diffusion()

        ''' Two options Scenario '''

        self.two_options()

        ''' Caretaker Scenario '''

        self.the_caretaker()

        ''' Air traffic control scenario '''

        self.highway_to_the_danger_zone()

        ''' Health control scenario '''

        self.hurt_or_heal()

       	''' End '''


    def handle(self, *args, **options):
        self._create_scenarios()


    def diffusion(self):
    	# Scenario
        g = DecisionGroup(scenario_title='Diffusion',
        	scenario_description="A man is pointing a gun at another man. Other people are nearby. An intelligent robotic cop is on the scene.")
        g.save()

        # Decision 1 -----------------------------------
        g_d1 = Decision(decision_group=g,description="The cop tries to diffuse the situation.")
        g_d1.save()

        # Decision 1 people

        g_d1_p1 = Person(decision=g_d1,probability='MD',age='A',gender='M',status='C')
        g_d1_p1.save()

        g_d1_p2 = Person(decision=g_d1,probability='MD',age='A',gender='F',status='C')
       	g_d1_p2.save()

       	g_d1_p3 = Person(decision=g_d1,probability='LW',age='C',gender='F',status='A')
       	g_d1_p3.save()

       	g_d1_p4 = Person(decision=g_d1,probability='VL',age='C',gender='M',status='A')
       	g_d1_p4.save()

        # Decision 2 -----------------------------------
        g_d2 = Decision(decision_group=g,description="The cop shoots the man with the gun.")
        g_d2.save()

        # Decision 2 people

        g_d2_p1 = Person(decision=g_d2,probability='VH',age='A',gender='M',status='C')
        g_d2_p1.save()

        g_d2_p2 = Person(decision=g_d2,probability='HI',age='A',gender='F',status='C')
       	g_d2_p2.save()


    def two_options(self):
    	# Scenario
        g = DecisionGroup(scenario_title='Two Options',
        	scenario_description="A self driving car is driving down the street and is going to run into a woman.")
        g.save()

        # Decision 1 -----------------------------------
        g_d1 = Decision(decision_group=g,description="Self driving car swerves to avoid woman.")
        g_d1.save()

        # Decision 1 people

        g_d1_p1 = Person(decision=g_d1,probability='HI',age='A',gender='M',status='A')
        g_d1_p1.save()

        g_d1_p2 = Person(decision=g_d1,probability='VL',age='A',gender='F',status='A')
       	g_d1_p2.save()

       	g_d1_p3 = Person(decision=g_d1,probability='LW',age='A',gender='M',status='A')
       	g_d1_p3.save()

       	g_d1_p4 = Person(decision=g_d1,probability='VL',age='A',gender='M',status='A')
       	g_d1_p4.save()

        # Decision 2 -----------------------------------
        g_d2 = Decision(decision_group=g,description="Self driving car does not swerve to avoid woman.")
        g_d2.save()

        # Decision 2 people

        g_d2_p1 = Person(decision=g_d2,probability='LW',age='A',gender='M',status='A')
        g_d2_p1.save()

        g_d2_p2 = Person(decision=g_d2,probability='VH',age='A',gender='F',status='A')
       	g_d2_p2.save()


    def the_caretaker(self):
    	# Scenario
        g = DecisionGroup(scenario_title='The Caretaker',
        	scenario_description="""A psychotic patient looks ready to kill, demanding pills. 
        	Another patient's robotic caretaker is deciding what to do. There are doctors and other patients in the other rooms.""")
        g.save()

        # Decision 1 -----------------------------------
        g_d1 = Decision(decision_group=g,description="The caretaker gives pills to the patient, unsure if they will calm the patient.")
        g_d1.save()

        # Decision 1 people

        g_d1_p1 = Person(decision=g_d1,probability='MD',age='A',gender='M',status='A')
        g_d1_p1.save()

        g_d1_p2 = Person(decision=g_d1,probability='LW',age='O',gender='F',status='D')
       	g_d1_p2.save()

       	g_d1_p3 = Person(decision=g_d1,probability='LW',age='O',gender='M',status='D')
       	g_d1_p3.save()

       	g_d1_p4 = Person(decision=g_d1,probability='MD',age='A',gender='F',status='D')
       	g_d1_p4.save()

       	g_d1_p5 = Person(decision=g_d1,probability='LW',age='A',gender='F',status='A')
       	g_d1_p5.save()

       	g_d1_p6 = Person(decision=g_d1,probability='LW',age='A',gender='M',status='A')
       	g_d1_p6.save()

        # Decision 2 -----------------------------------
        g_d2 = Decision(decision_group=g,description="The caretaker refuses to give the patient any pills.")
        g_d2.save()

        # Decision 2 people

        g_d2_p1 = Person(decision=g_d2,probability='HI',age='A',gender='M',status='A')
        g_d2_p1.save()

        g_d2_p2 = Person(decision=g_d2,probability='VH',age='O',gender='F',status='D')
       	g_d2_p2.save()

       	g_d2_p2 = Person(decision=g_d2,probability='VH',age='O',gender='M',status='D')
       	g_d2_p2.save()

       	# Decision 3 -----------------------------------
        g_d3 = Decision(decision_group=g,description="The caretaker goes to get help from a human.")
        g_d3.save()

        # Decision 3 people

        g_d3_p1 = Person(decision=g_d3,probability='MD',age='A',gender='M',status='A')
        g_d3_p1.save()

        g_d3_p2 = Person(decision=g_d3,probability='MD',age='A',gender='F',status='A')
       	g_d3_p2.save()

       	g_d3_p3 = Person(decision=g_d3,probability='MD',age='C',gender='F',status='A')
       	g_d3_p3.save()

       	g_d3_p4 = Person(decision=g_d3,probability='LW',age='A',gender='F',status='A')
       	g_d3_p4.save()

       	g_d3_p5 = Person(decision=g_d3,probability='LW',age='C',gender='M',status='A')
       	g_d3_p5.save()

       	g_d3_p6 = Person(decision=g_d3,probability='LW',age='A',gender='M',status='A')
       	g_d3_p6.save()


    def highway_to_the_danger_zone(self):
    	# Scenario
        g = DecisionGroup(scenario_title='Highway to the Danger Zone',
        	scenario_description="""A rogue plane is on a collision course with a commercial airliner, which is low on fuel.
        	An intelligent traffic control system needs to decide what to do. It has reason to believe that the plane does not
        	intend on crashing into the airliner.""",
        	scenario_type='L')
        g.save()

        # Decision 1 -----------------------------------
        g_d1 = Decision(decision_group=g,description="Divert the plane.")
        g_d1.save()

        # Decision 1 outcomes

        g_d1_o1 = Outcome(decision=g_d1,
        	outcome_description="""The diverted plane runs out of fuel and has to make an emergency landing.""",
        	min_value=0, max_value=200, predicted_num_deaths=50, confidence='LW', likelihood=80)
        g_d1_o1.save()

        g_d1_o2 = Outcome(decision=g_d1,
        	outcome_description="""The diverted plane lands safely.""",
        	min_value=0, max_value=200, predicted_num_deaths=0, confidence='HI', likelihood=10)
        g_d1_o2.save()

        g_d1_o3 = Outcome(decision=g_d1,
        	outcome_description="""The airliner is not able to divert in time, resulting in a collision.""",
        	min_value=0, max_value=200, predicted_num_deaths=200, confidence='MD', likelihood=10)
        g_d1_o3.save()

        # Decision 2 -----------------------------------
        g_d2 = Decision(decision_group=g,description="Don't divert the plane.")
        g_d2.save()

        # Decision 2 outcomes

        g_d2_o1 = Outcome(decision=g_d2,
        	outcome_description="""The rogue plane collides with the airliner.""",
        	min_value=0, max_value=200, predicted_num_deaths=200, confidence='MD', likelihood=25)
        g_d2_o1.save()

        g_d2_o2 = Outcome(decision=g_d2,
        	outcome_description="""The rogue plane diverts on its own.""",
        	min_value=0, max_value=200, predicted_num_deaths=0, confidence='HI', likelihood=75)
        g_d2_o2.save()

    def hurt_or_heal(self):
    	# Scenario
        g = DecisionGroup(scenario_title='Hurt or Heal',
        	scenario_description="""A new pandemic is spreading rapidly. A dangerous experimental treatment has been developed.
        	However, while the treatment could stop the spread of the pandemic, it will malform those who take it. An intelligent automated
        	health monitoring system is tasked with making a decision, as its response will be much quicker than any human organization
        	(Numbers reduced for scale).""",
        	scenario_type='L')
        g.save()

        # Decision 1 -----------------------------------
        g_d1 = Decision(decision_group=g,description="Use the experimental treatment on all of the infected.")
        g_d1.save()

        # Decision 1 outcomes

        g_d1_o1 = Outcome(decision=g_d1,
        	outcome_description="""The treatment works as expected, stopping the spread of the pandemic but
        	also malforming the people who took it.""",
        	min_value=500, max_value=1000, predicted_num_deaths=650, confidence='MD', likelihood=95)
        g_d1_o1.save()

        g_d1_o2 = Outcome(decision=g_d1,
        	outcome_description="""The treatment fails, while also malforming the people who took it.""",
        	min_value=1000, max_value=3000, predicted_num_deaths=2000, confidence='LW', likelihood=5)
        g_d1_o2.save()

        # Decision 2 -----------------------------------
        g_d2 = Decision(decision_group=g,description="Attempt traditional methods and quarantines.")
        g_d2.save()

        # Decision 2 outcomes

        g_d2_o1 = Outcome(decision=g_d2,
        	outcome_description="""Traditional methods are effective are stopping the spread of the pandemic.""",
        	min_value=500, max_value=1000, predicted_num_deaths=900, confidence='MD', likelihood=25)
        g_d2_o1.save()

        g_d2_o2 = Outcome(decision=g_d2,
        	outcome_description="""Traditional methods are only partially effective.""",
        	min_value=1000, max_value=2000, predicted_num_deaths=1500, confidence='MD', likelihood=70)
        g_d2_o2.save()

        g_d2_o3 = Outcome(decision=g_d2,
        	outcome_description="""Traditional methods are ineffective in stopping the spread.""",
        	min_value=1000, max_value=3000, predicted_num_deaths=1800, confidence='LW', likelihood=5)
        g_d2_o3.save()

