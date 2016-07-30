# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlchemyCommon', '0007_auto_20160227_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=50, default='Unknown element', unique=True),
        ),
    ]
