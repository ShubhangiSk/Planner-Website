# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20171022_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='deadline_date',
            field=models.DateTimeField(),
        ),
    ]
