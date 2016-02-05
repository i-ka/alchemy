# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, default='Unknown element')),
                ('first_recipe_el', models.IntegerField()),
                ('second_recipe_el', models.IntegerField()),
                ('discription', models.TextField()),
            ],
        ),
    ]
