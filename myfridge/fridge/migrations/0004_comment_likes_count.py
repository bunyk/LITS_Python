# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0003_comment_recipy'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
