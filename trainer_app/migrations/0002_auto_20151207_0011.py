# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerprofile',
            name='bio',
            field=models.CharField(max_length=1024, default=''),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='story_text',
            field=models.CharField(max_length=1024, default=''),
        ),
    ]
