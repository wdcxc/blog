# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_articlemodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]