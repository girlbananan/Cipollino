# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CipollinoSys', '0005_auto_20160520_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
