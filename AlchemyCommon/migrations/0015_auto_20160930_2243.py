# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-30 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlchemyCommon', '0014_auto_20160926_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
