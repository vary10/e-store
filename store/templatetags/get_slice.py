from django.template import Library

register = Library()

@register.filter
def get_slice(value, arg):
    a, b, c = arg.split(":")
    if not a:
        a = 0
    if not b:
        b = len(value) - 1
    if not c:
        c = 1
    a, b, c = list(map(int, [a, b, c]))
    if a < 0:
        a += len(value)
    if b < 0:
        b += len(value)
    return value[a:b:c]