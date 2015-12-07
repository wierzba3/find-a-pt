# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_app', '0003_auto_20151207_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='profile',
            field=models.ForeignKey(to='trainer_app.TrainerProfile'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='profile',
            field=models.ForeignKey(to='trainer_app.TrainerProfile'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='profile',
            field=models.ForeignKey(to='trainer_app.TrainerProfile'),
        ),
    ]
