# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_one', '0002_auto_20151022_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListFailureFiltering',
            fields=[
                ('listfailure_ptr', models.OneToOneField(auto_created=True, primary_key=True, to='type_one.ListFailure', parent_link=True, serialize=False)),
                ('station_name_1', models.ForeignKey(blank=True, null=True, verbose_name='Станция', to='type_one.Station')),
            ],
            bases=('type_one.listfailure', models.Model),
        ),
    ]
