# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 07:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0004_auto_20170808_0737'),
    ]

    # operations = [
    #     migrations.AlterField(
    #         model_name='profile',
    #         name='current_user',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
    #     ),
    # ]