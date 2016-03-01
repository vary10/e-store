from django.template import Library

register = Library()

@register.filter
def get_by_index(value, arg):
    i = int(arg)
    try:
        if i < 0:
            i += len(value)
        return [value[i]]
    except:
        print("NO SUCH INDEX")