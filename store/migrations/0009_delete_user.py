# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-14 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20160514_1225'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]