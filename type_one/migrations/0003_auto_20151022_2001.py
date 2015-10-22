# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_one', '0002_auto_20151022_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failuretype',
            name='failure_type',
            field=models.CharField(max_length=50),
        ),
    ]
