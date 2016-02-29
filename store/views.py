from django.shortcuts import render, get_object_or_404, redirect
import django.utils
from .models import Item
from django.http import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "home.html", {'items': items})


def info(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "item.html", {"items": items})


def profile(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "profile.html", {'items': items})


def cart(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "cart.html", {'items': items})

def add(request):
    return HttpResponse("Added")


# def choose_item(request):
#     return redirect('info_by_item', item_id=request.POST['item'])
#
# def info_by_item(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)
#     return render(request, 'info.html', {'item': item})
# class ProductView(TemplateView):
#     template_name = "item.html"
#
#     def get(self, request, *args, **kwargs):
#         context = super().get(self, request, *args, **kwargs)
#         print(request, *args, **kwargs)
#         context['item'] = Item.objects.filter
#         return context
