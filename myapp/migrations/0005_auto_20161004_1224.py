# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20161004_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='image',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
