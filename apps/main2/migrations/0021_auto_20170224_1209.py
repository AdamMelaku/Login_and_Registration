# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20170224_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=id, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='main.User'),
        ),
    ]