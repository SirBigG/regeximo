# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitelog',
            name='text',
            field=models.TextField(db_index=True, verbose_name='Log line content'),
        ),
    ]
