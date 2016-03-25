from django.template import Library

register = Library()

@register.filter
def sep(value):
    value = value.replace("-", "+")
    value = "-".join(value.split())
    value = value.lower()
    return value