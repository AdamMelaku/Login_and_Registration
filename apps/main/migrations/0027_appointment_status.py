# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20170224_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
    ]