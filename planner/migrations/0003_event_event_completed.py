# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20171021_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_completed',
            field=models.BooleanField(default=False),
        ),
    ]