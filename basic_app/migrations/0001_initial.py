# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-26 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('status', models.CharField(blank=True, max_length=64)),
                ('created_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
