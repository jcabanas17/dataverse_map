# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0013_auto_20160720_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='version',
            field=models.CharField(default='3.6', max_length=6),
        ),
        migrations.AlterField(
            model_name='institution',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='installations.Installation'),
        ),
    ]
