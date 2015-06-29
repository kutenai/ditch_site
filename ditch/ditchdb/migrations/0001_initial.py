# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DitchCal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ditch_slope', models.FloatField()),
                ('ditch_scale', models.FloatField()),
                ('sump_slope', models.FloatField()),
                ('sump_scale', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DitchLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('ditchlvl', models.IntegerField()),
                ('sumplvl', models.IntegerField()),
                ('pump_call', models.BooleanField()),
                ('pump_on', models.BooleanField()),
                ('north_call', models.BooleanField()),
                ('north_on', models.BooleanField()),
                ('south_call', models.BooleanField()),
                ('south_on', models.BooleanField()),
            ],
        ),
    ]
