# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0013_auto_20171023_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 15, 48, 17, 105328)),
        ),
    ]
