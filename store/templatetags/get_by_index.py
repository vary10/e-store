from django.template import Library

register = Library()

@register.filter
def get_by_index(value, arg):
    i = int(arg)
    try:
        if i < 0:
            i += len(value)
        if i >= len(value):
            i = len(value) - 1
        return [value[i]]
    except:
        print("NO SUCH INDEX")