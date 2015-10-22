# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, to=settings.AUTH_USER_MODEL, parent_link=True, primary_key=True, serialize=False)),
                ('day_of_birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FailureType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('failure_type', models.CharField(max_length=50, choices=[('Critical', (('Ethernet link down', 'Ethernet link down'), ('Crit_2', 'Crit_2'))), ('Major', (('Major_1', 'Major_1'), ('Major_2', 'Major_2')))])),
            ],
            options={
                'ordering': ['failure_type'],
            },
        ),
        migrations.CreateModel(
            name='ListFailure',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time_on', models.DateField(verbose_name='Дата начала')),
                ('time_off', models.DateField(verbose_name='Дата окончания')),
                ('time_1', models.TimeField(verbose_name='Время начала')),
                ('time_2', models.TimeField(verbose_name='Время окончания')),
                ('delt_time', models.DurationField(blank=True, null=True)),
                ('fio_name', models.CharField(max_length=20)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('username', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['time_on'],
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('station_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['station_name'],
            },
        ),
        migrations.CreateModel(
            name='ListFailureFiltering',
            fields=[
                ('listfailure_ptr', models.OneToOneField(auto_created=True, to='type_one.ListFailure', parent_link=True, primary_key=True, serialize=False)),
                ('station_name_1', models.ForeignKey(to='type_one.Station', null=True, verbose_name='Станция', blank=True)),
            ],
            bases=('type_one.listfailure', models.Model),
        ),
        migrations.AddField(
            model_name='listfailure',
            name='station_name',
            field=models.ForeignKey(to='type_one.Station', verbose_name='Cтанция'),
        ),
        migrations.AddField(
            model_name='listfailure',
            name='type_of_failure',
            field=models.ForeignKey(to='type_one.FailureType', verbose_name='Тип повреждения'),
        ),
    ]
