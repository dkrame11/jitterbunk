# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-06-17 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bunk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_user', to='bunk.UserProfile'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_user', to='bunk.UserProfile'),
        ),
    ]