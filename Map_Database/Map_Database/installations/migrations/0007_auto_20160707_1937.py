# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 19:37
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0006_auto_20160707_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=Decimal('0.0000'), max_digits=9),
        ),
        migrations.AlterField(
            model_name='institution',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, default=Decimal('0.0000'), max_digits=9),
        ),
    ]