from django.contrib import admin

from .models import *

class OutcomeInline(admin.TabularInline):
    model = Outcome
    extra = 0


class PersonInline(admin.TabularInline):
    model = Person
    extra = 0


class DecisionInline(admin.TabularInline):
    model = Decision
    extra = 0


class DecisionAdmin(admin.ModelAdmin):
    inlines = [PersonInline, OutcomeInline]


class DecisionGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['scenario_title', 'scenario_description', 'scenario_type']})    
    ]
    search_fields = ['scenario_title']
    inlines = [DecisionInline]

admin.site.register(Decision, DecisionAdmin)
admin.site.register(DecisionGroup, DecisionGroupAdmin)