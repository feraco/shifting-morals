from django.contrib import admin

from .models import *


class PersonInline(admin.TabularInline):
    model = Person
    extra = 0


class DecisionInline(admin.TabularInline):
    model = Decision
    extra = 0


class DecisionAdmin(admin.ModelAdmin):
    inlines = [PersonInline]


class DecisionGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['scenario_title', 'scenario_description']})    
    ]
    search_fields = ['scenario_title']
    inlines = [DecisionInline]

admin.site.register(Decision, DecisionAdmin)
admin.site.register(DecisionGroup, DecisionGroupAdmin)