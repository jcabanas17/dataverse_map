# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0004_auto_20160707_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='host',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='installations.installation'),
            preserve_default=False,
        ),
    ]