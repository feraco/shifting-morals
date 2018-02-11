from django.contrib import admin

from .models import *


class PersonInline(admin.TabularInline):
    model = Person
    extra = 1


class DecisionInline(admin.TabularInline):
    model = Decision
    extra = 1


class DecisionAdmin(admin.ModelAdmin):
    inlines = [PersonInline]


class DecisionGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['scenario_text']})    
    ]
    search_fields = ['scenario_text']
    inlines = [DecisionInline]

admin.site.register(Decision, DecisionAdmin)
admin.site.register(DecisionGroup, DecisionGroupAdmin)