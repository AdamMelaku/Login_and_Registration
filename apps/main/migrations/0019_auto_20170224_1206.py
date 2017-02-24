# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20170224_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ManyToManyField(related_name='appointments', to='main.User'),
        ),
    ]
