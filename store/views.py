from django.shortcuts import render, get_object_or_404
import django.utils
from .models import Item
from django.http import HttpResponse


def home(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "home.html", {'items': items})


def profile(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "profile.html", {'items': items})


def cart(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "cart.html", {'items': items})


def add(request):
    return HttpResponse("Added")


def info(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item.html', {'item': item})