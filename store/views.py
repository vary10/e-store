from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import django.utils
from .models import Item, ItemForm, Cart, CartItem, Payment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm


def accounts_login(request):
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a> <a href='/login/facebook/?next=\
                            http://127.0.0.1:8000/'>login with Facebook</a>")


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('/')


@login_required
def account_profile(request):
    check_cart(request)
    return redirect("/")


@login_required
def profile(request):
    my_items = Item.objects.filter(creator=request.user).order_by('published_date')
    bought_items = Item.objects.all()
    return render(request, "profile.html", {'my_items': my_items, "bought_items": bought_items})


def home(request):
    items = Item.objects.filter(published_date__lte=django.utils.timezone.now()).order_by('published_date')
    return render(request, "home.html", {'items': items})


@login_required
def check_cart(request):
    if not Cart.objects.filter(owner=request.user,paid=False).order_by("date_created"):
        tmp = Cart.objects.latest("date_created")

        new_cart = Cart()
        new_cart.owner = request.user
        new_cart.invoice = tmp.invoice + 1
        new_cart.save()


@login_required
def create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.creator = request.user
            new_item.save()
            form.save_m2m()
            return HttpResponse("<p>Success! Now wait for the publication.</p><a href='/'>Home</a>")
        return HttpResponse("<p>Something went wrong, <a href='{0}'>go back</a>".format(request.META["HTTP_REFERER"]))
    else:
        form = ItemForm()
    return render(request, "product_form.html", {'formset': form})


def info(request, item_title):
    item_title = str(item_title).replace("-", " ")
    item_title = item_title.replace("+", "-")
    item = get_object_or_404(Item, title__iexact=item_title)
    return render(request, 'item.html', {'item': item})


@login_required
def cart(request):
    check_cart(request)
    paypal_dict = {
        "business": "vary10-facilitator@gmail.com",
        "currency_code": "RUB",
        "item_name": "products in store",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://127.0.0.1:8000/payment/success/",
        "cancel_return": "http://127.0.0.1:8000/cart/",
        "custom": str(request.user.id)
    }
    # Create the instance.
    cart = Cart.objects.filter(owner=request.user, paid=False).latest('date_created')
    items = cart.cartitem_set.all()
    paypal_dict["amount"] = cart.total()
    paypal_dict["invoice"] = cart.invoice

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict, "items": items, "cart": cart}
    return render(request, "cart.html", context)


def add(request):
    check_cart(request)
    cart = Cart.objects.filter(owner=request.user, paid=False).latest('date_created')
    it = CartItem.objects.filter(item_id=int(request.POST.get('item')[4:]), cart=cart)
    if not it:
        new_cart_item = CartItem()
        new_cart_item.item = Item.objects.get(id=int(request.POST.get('item')[4:]))
        new_cart_item.cart = cart
        new_cart_item.number = 1
        new_cart_item.save()
    else:
        print(it[0])
        it[0].number = it[0].number + 1
        it[0].save()
    return HttpResponse("Added")


def delete(request):
    CartItem.objects.filter(id=int(request.POST.get('item')[4:])).delete()
    return redirect("/info/")


@csrf_exempt
def paypal_success(request):
    cart = Cart.objects.filter(owner=request.user, paid=False).latest('date_created')
    cart.paid = True
    for cart_item in cart.cartitem_set.all():
        cart_item.item.gathered += cart_item.total()
        cart_item.item.save()
    cart.save()
    return HttpResponse("Money is mine. Thanks.")