# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-19 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='was_viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='last_update',
            field=models.DateField(default=datetime.date(2020, 5, 19)),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('monitored', 'monitored'), ('irrelevant', 'irrelevant'), ('refuse', 'refuse')], default=('pending', 'pending'), max_length=10),
        ),
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
