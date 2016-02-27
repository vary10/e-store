from django.template import Library

register = Library()

@register.filter
def get_one_l(value, i):
  if i >= len(value):
    return [value[0]]
  return [value[len(value)-i]]