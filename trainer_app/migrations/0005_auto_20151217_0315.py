# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_app', '0004_auto_20151207_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificationEnum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('certification_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='GymEnum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('gym_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='certification',
            name='certification_name',
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='education',
            field=models.CharField(max_length=256, default='Not specified'),
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='gender',
            field=models.CharField(max_length=64, default='Male'),
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='online_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='rate',
            field=models.CharField(max_length=256, default='Not specified'),
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='trains_at',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='specialty_type',
            field=models.ForeignKey(to='client_app.GoalEnum'),
        ),
        migrations.AlterField(
            model_name='trainerprofile',
            name='bio',
            field=models.CharField(max_length=1024, default='No bio'),
        ),
        migrations.DeleteModel(
            name='SpecialtyType',
        ),
        migrations.AddField(
            model_name='gym',
            name='gym_type',
            field=models.ForeignKey(to='trainer_app.GymEnum'),
        ),
        migrations.AddField(
            model_name='gym',
            name='profile',
            field=models.ForeignKey(to='trainer_app.TrainerProfile'),
        ),
        migrations.AddField(
            model_name='certification',
            name='certification_type',
            field=models.ForeignKey(to='trainer_app.CertificationEnum', null=True),
        ),
    ]
