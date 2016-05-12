from django.db import models
import django.utils
from django.contrib.auth.models import User


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


class User(models.Model):
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d")


class Cart(models.Model):
    date_created = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    date_modified = models.DateTimeField(default=django.utils.timezone.now, editable=True)
    total = models.IntegerField()
    payed = models.BooleanField(False)
    items = models.ManyToManyField(Item)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
    )


class Payment(models.Model):
    pp_id = models.CharField(max_length=40)
    date = models.DateTimeField()
    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        primary_key=False,
    )

