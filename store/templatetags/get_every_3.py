from django.template import Library

register = Library()

@register.filter
def get_every_3(value, i):
    return value[3 * i:3 * i + 3]