# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ditchdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ditchcal',
            name='ditch_alarm',
            field=models.FloatField(default=50),
        ),
        migrations.AddField(
            model_name='ditchcal',
            name='ditch_empty',
            field=models.FloatField(default=720),
        ),
        migrations.AlterField(
            model_name='ditchcal',
            name='ditch_scale',
            field=models.FloatField(default=14.0),
        ),
        migrations.AlterField(
            model_name='ditchcal',
            name='ditch_slope',
            field=models.FloatField(default=-0.0106),
        ),
        migrations.AlterField(
            model_name='ditchcal',
            name='sump_scale',
            field=models.FloatField(default=0.037),
        ),
        migrations.AlterField(
            model_name='ditchcal',
            name='sump_slope',
            field=models.FloatField(default=-3.034),
        ),
    ]
