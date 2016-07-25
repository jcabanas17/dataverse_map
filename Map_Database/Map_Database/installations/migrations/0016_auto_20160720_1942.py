# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0015_auto_20160720_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='installations.Installation'),
        ),
    ]
