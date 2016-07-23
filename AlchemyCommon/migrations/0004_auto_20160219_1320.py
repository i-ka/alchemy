# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AlchemyCommon', '0003_ueserprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('my_field', models.CharField(max_length=50, default='Europe/London')),
                ('user', models.ForeignKey(unique=True, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ueserprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UeserProfile',
        ),
    ]
