# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0010_auto_20170824_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemodel',
            old_name='date_archive',
            new_name='date_archives',
        ),
    ]
