# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='booby', max_length=255),
            preserve_default=False,
        ),
    ]
