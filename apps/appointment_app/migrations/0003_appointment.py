# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170224_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('date', models.DateField(max_length=8)),
                ('time', models.TimeField()),
            ],
        ),
    ]
