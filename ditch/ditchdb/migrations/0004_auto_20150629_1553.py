# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ditchdb', '0003_auto_20150629_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ditchlog',
            name='ditch_inches',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='ditchlvl',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='north_call',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='north_on',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='pump_call',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='pump_on',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='south_call',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='south_on',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='sump_inches',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='ditchlog',
            name='sumplvl',
            field=models.IntegerField(default=0),
        ),
    ]
