# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_app', '0002_auto_20151207_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='specialty',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='user',
            new_name='profile',
        ),
    ]
