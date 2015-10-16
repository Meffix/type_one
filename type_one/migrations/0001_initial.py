# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('day_of_birthday', models.DateField(verbose_name='Дата рождения', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Failure_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('failure_type', models.CharField(choices=[('Critical', (('Crit_1', 'Crit_1'), ('Crit_2', 'Crit_2'))), ('Major', (('Major_1', 'Major_1'), ('Major_2', 'Major_2')))], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fio',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='List_failure',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('time_on', models.DateField(verbose_name='Дата начала повреждения')),
                ('time_off', models.DateField(verbose_name='Дата окончания повреждения')),
                ('time_1', models.TimeField(verbose_name='Время начала')),
                ('time_2', models.TimeField(verbose_name='Время окончания')),
                ('delt_time', models.DurationField(blank=True, null=True)),
                ('fio_name', models.CharField(max_length=20)),
                ('comment', models.TextField(verbose_name='Комментарии', blank=True, null=True)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('station_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='List_failure_for_filtering',
            fields=[
                ('list_failure_ptr', models.OneToOneField(to='type_one.List_failure', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('station_name_1', models.ForeignKey(to='type_one.Station', verbose_name='Выберите станцию', blank=True, null=True)),
            ],
            bases=('type_one.list_failure', models.Model),
        ),
        migrations.AddField(
            model_name='list_failure',
            name='station_name',
            field=models.ForeignKey(verbose_name='Название станцию', to='type_one.Station'),
        ),
        migrations.AddField(
            model_name='list_failure',
            name='type_of_failure',
            field=models.ForeignKey(verbose_name='Тип повреждения', to='type_one.Failure_type'),
        ),
    ]
