# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 22:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='idade',
            field=models.PositiveIntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
