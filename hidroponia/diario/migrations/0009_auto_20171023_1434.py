# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 16:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0008_auto_20171023_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 14, 34, 36, 302904)),
        ),
    ]
