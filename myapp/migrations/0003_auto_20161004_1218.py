# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_basesubtopic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basesubtopic',
            name='topic',
        ),
        migrations.DeleteModel(
            name='BaseSubTopic',
        ),
    ]
