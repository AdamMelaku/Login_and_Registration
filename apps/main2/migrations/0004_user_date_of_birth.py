# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]
