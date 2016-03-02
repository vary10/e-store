# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gathered',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='goal',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
