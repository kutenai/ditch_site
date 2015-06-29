# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditchdb', '0002_auto_20150629_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='ditchlog',
            name='ditch_inches',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ditchlog',
            name='sump_inches',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
