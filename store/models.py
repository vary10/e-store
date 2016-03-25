from django.db import models
import django.utils


class Item(models.Model):
    author = models.ForeignKey('auth.User')
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
    name = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d")