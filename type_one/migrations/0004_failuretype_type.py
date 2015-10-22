# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_one', '0003_auto_20151022_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='failuretype',
            name='type',
            field=models.CharField(max_length=50, default=2),
            preserve_default=False,
        ),
    ]
