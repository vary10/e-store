from django.shortcuts import render
from django.utils import timezone
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "store/home.html", {'items': items})

def info(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "store/item.html", {"info": items[0]})

def profile(request):
    return render(request, "store/profile.html", {})

#def cart(request):
#    return render(request, "store/cart.html", {})
