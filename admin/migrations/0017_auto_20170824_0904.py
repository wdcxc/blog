# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0016_auto_20170824_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datearchivemodel',
            name='pre_grade',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_grades', related_query_name='next_grade', to='admin.DateArchiveModel'),
        ),
    ]