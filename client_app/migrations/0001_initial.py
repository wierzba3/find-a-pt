# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=64, default='Male')),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceEnum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('experience_text', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoalEnum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('goal_text', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingTimeEnum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('training_time', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingTypeEnum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('training_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('client', models.OneToOneField(to='client_app.ClientProfile', primary_key=True, serialize=False)),
                ('other_details', models.CharField(max_length=512, default='')),
                ('experience', models.ForeignKey(to='client_app.ExperienceEnum', on_delete=django.db.models.deletion.SET_NULL, null=True)),
                ('training_type', models.ForeignKey(to='client_app.TrainingTypeEnum', on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='trainingtime',
            name='training_time_type',
            field=models.ForeignKey(to='client_app.TrainingTimeEnum'),
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_type',
            field=models.ForeignKey(to='client_app.GoalEnum'),
        ),
        migrations.AddField(
            model_name='trainingtime',
            name='goals',
            field=models.ForeignKey(to='client_app.Goals'),
        ),
        migrations.AddField(
            model_name='goal',
            name='goals',
            field=models.ForeignKey(to='client_app.Goals'),
        ),
    ]
