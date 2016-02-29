from django.shortcuts import render
from django.utils import timezone
from .models import Item


# Create your views here.
def home(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "home.html", {'items': items})


def info(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "item.html", {"items": items})


def profile(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "profile.html", {'items': items})


def cart(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "cart.html", {'items': items})

# class ProductView(TemplateView):
#     template_name = "store/product.html"
#
#     def get_context_data(self, context ...):
#         context = super().get_context_data(context)
#         context['item'] = Items.objects.get_or_404(id=self.request.GET.args?['slug'])
#         return context
