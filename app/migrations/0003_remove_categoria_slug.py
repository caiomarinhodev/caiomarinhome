# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-31 23:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160831_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
    ]
