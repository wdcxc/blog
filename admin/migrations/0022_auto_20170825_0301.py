# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0021_articlemodel_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='meta',
            field=models.TextField(null=True),
        ),
    ]