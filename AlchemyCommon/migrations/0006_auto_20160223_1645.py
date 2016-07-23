# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('AlchemyCommon', '0005_auto_20160219_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='my_field',
            new_name='open_elements',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile'),
        ),
    ]
