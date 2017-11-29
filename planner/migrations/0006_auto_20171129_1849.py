# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20171022_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('official_event', 'Official Event'), ('personal_event', 'Personal Event'), ('fun_event', 'Fun Event')], default='personal_event', max_length=20),
        ),
        migrations.AddField(
            model_name='event',
            name='priority',
            field=models.IntegerField(choices=[(1, 'High Priority'), (2, 'Medium Priority'), (3, 'Low Priority')], default=1),
        ),
    ]
