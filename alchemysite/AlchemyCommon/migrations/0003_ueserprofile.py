# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AlchemyCommon', '0002_element_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UeserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('my_field', models.CharField(max_length=50, default='Europe/London')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='profile', unique=True)),
            ],
        ),
    ]
