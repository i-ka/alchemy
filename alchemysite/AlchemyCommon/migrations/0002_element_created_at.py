# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AlchemyCommon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='created_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 5, 8, 33, 54, 179045, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
