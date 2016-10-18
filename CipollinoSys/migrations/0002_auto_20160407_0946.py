# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 09:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CipollinoSys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_link', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='nickname',
        ),
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.CharField(default='zeroDep', max_length=10),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='Новая', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='task_performer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_performer', to='CipollinoSys.Person'),
        ),
        migrations.AddField(
            model_name='task',
            name='wasted_time',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_owner',
        ),
        migrations.AddField(
            model_name='task',
            name='task_owner',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='company',
            name='company_boss',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CipollinoSys.Person'),
        ),
    ]
