# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0006_auto_20170822_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='categories',
            field=models.ManyToManyField(related_name='articles', related_query_name='article', to='admin.CategoryModel'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='tags',
            field=models.ManyToManyField(related_name='articles', related_query_name='article', to='admin.TagModel'),
        ),
    ]