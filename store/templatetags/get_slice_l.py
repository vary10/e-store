from django.template import Library

register = Library()

@register.filter
def get_slice_l(value, i):
  if i >= len(value):
    return value[1:]
  else:
    return value[len(value)-i:]