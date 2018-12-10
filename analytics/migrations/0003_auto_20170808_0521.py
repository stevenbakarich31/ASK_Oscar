# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0002_profile_current_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_average_order_value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_bounce_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_conversion_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_revenue_per_user',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_shopping_cart_abandonment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_average_order_value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_bounce_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_conversion_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_revenue',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_revenue_per_user',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_shopping_cart_abandonment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='optimal_traffic',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='revenue_last_month',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='revenue_this_month',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='traffic_last_month',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='traffic_this_month',
            field=models.FloatField(default=0),
        ),
    ]