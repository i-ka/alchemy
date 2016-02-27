# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlchemyCommon', '0006_auto_20160223_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='Unknown category', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='element',
            name='category',
            field=models.ForeignKey(default=1223, to='AlchemyCommon.Category'),
            preserve_default=False,
        ),
    ]
