from django.db import models
import django.utils
from django.contrib.auth.models import User
from django.forms import ModelForm


class Item(models.Model):
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=django.utils.timezone.now, editable=False)
    published_date = models.DateTimeField(
            blank=True, null=True)
    cpu = models.IntegerField()
    goal = models.IntegerField()
    gathered = models.IntegerField(default=0)
    image = models.ImageField(upload_to="%Y/%m/%d/", height_field=None, width_field=None, max_length=100)

    def save(self, *args, **kwargs):
        self.full_clean() # performs regular validation then clean()
        super(Item, self).save(*args, **kwargs)

    def clean(self):
        if self.title:
            self.title = " ".join(self.title.split())

    def __str__(self):
        return self.title

    def percentage(self):
        return int(self.gathered / self.goal * 100)


# class User(models.Model):
#     email = models.CharField(max_length=25)
#     password = models.CharField(max_length=25)
#     name = models.CharField(max_length=25)
#     avatar = models.ImageField(upload_to="avatars/%Y/%m/%d")


class Cart(models.Model):
    date_created = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    date_modified = models.DateTimeField(default=django.utils.timezone.now, editable=True)
    paid = models.BooleanField(default=False)
    invoice = models.IntegerField(default=2)

    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        primary_key=False,
    )
    def total(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.total()
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, primary_key=False)
    number = models.IntegerField(editable=True)

    def total(self):
        return self.number * self.item.cpu



class Payment(models.Model):
    pp_id = models.CharField(max_length=40)
    date = models.DateTimeField()
    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        primary_key=False,
    )

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'cpu', 'goal']