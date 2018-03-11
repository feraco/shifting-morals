from django import template

register = template.Library()

# From https://stackoverflow.com/questions/4731572/django-counter-in-loop-to-index-list
# Thanks to user Caumons
@register.filter
def index(sequence, position):
        return sequence[position]
