# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0004_auto_20171122_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.User'),
            preserve_default=False,
        ),
    ]
