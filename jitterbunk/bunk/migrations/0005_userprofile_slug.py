# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-06-18 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunk', '0004_remove_userprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='Reset', unique=True),
        ),
    ]
