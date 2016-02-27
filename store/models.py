from django.db import models
from django.utils import timezone


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    cpu = models.IntegerField()
    image = models.ImageField(upload_to="%Y/%m/%d/", height_field=None, width_field=None, max_length=100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
