# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('link', models.URLField()),
                ('hits', models.IntegerField(default=0)),
                ('short_url', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
