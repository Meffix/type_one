# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_one', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listfailurefiltering',
            name='listfailure_ptr',
        ),
        migrations.RemoveField(
            model_name='listfailurefiltering',
            name='station_name_1',
        ),
        migrations.DeleteModel(
            name='ListFailureFiltering',
        ),
    ]
