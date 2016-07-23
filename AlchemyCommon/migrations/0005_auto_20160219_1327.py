# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlchemyCommon', '0004_auto_20160219_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='my_field',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='my_field',
            field=models.ManyToManyField(to='AlchemyCommon.Element'),
        ),
    ]
