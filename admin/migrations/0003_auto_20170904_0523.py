# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_auto_20170904_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='reply_comments',
            field=models.ManyToManyField(related_name='_commentmodel_reply_comments_+', related_query_name='replied_comment', to='admin.CommentModel'),
        ),
    ]
