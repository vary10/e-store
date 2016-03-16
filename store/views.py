from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import django.utils
from .models import Item
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm


def accounts_login(request):
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a> <a href='/login/facebook/?next=https://vary10.pythonanywhere.com/'>login with Facebook</a>")

def home(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "home.html", {'items': items})

@login_required
def account_profile(request):
    """
    Show user greetings. ONly for logged in users.
    """
    # ("Hi, {0}! Nice to meet you.".format(request.user.first_name))
    return redirect("/")

def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('/')

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

@csrf_exempt
def paypal_success(request):
    return HttpResponse("Money is mine. Thanks.")

@login_required
def paypal_pay(request):
    paypal_dict = {
        "business": "vary10-facilitator_api1.gmail.com",
        "amount": "100.00",
        "currency_code": "RUB",
        "item_name": "products in store",
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://vary10.pythonanywhere.com/payment/success/",
        "cancel_return": "http://vary10.pythonanywhere.com/payment/cart/",
        "custom": str(request.user.id)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict}
    return render(request, "payment.html", context)

