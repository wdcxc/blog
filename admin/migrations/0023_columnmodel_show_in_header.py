# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0022_auto_20170825_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='columnmodel',
            name='show_in_header',
            field=models.BooleanField(default=False),
        ),
    ]
