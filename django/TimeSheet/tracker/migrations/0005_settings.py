# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20151221_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_info', models.CharField(max_length=15)),
                ('created', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]