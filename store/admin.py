from django.contrib import admin
from .models import Item, Cart, CartItem, Payment

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(CartItem)
