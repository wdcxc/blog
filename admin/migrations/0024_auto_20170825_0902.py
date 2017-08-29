# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0023_columnmodel_show_in_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columnmodel',
            name='show_in_header',
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='show_in_header',
            field=models.BooleanField(default=False),
        ),
    ]