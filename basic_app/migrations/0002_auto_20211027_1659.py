# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-27 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_names', models.CharField(max_length=40)),
                ('Email_address', models.EmailField(max_length=254)),
                ('Content', models.TextField(max_length=260)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Names',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
