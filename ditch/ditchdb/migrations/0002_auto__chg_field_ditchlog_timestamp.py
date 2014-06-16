# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DitchLog.timestamp'
        db.alter_column(u'ditchdb_ditchlog', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):

        # Changing field 'DitchLog.timestamp'
        db.alter_column(u'ditchdb_ditchlog', 'timestamp', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'ditchdb.ditchcal': {
            'Meta': {'object_name': 'DitchCal'},
            'ditch_scale': ('django.db.models.fields.FloatField', [], {}),
            'ditch_slope': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sump_scale': ('django.db.models.fields.FloatField', [], {}),
            'sump_slope': ('django.db.models.fields.FloatField', [], {})
        },
        u'ditchdb.ditchlog': {
            'Meta': {'object_name': 'DitchLog'},
            'ditchlvl': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'north_call': ('django.db.models.fields.BooleanField', [], {}),
            'north_on': ('django.db.models.fields.BooleanField', [], {}),
            'pump_call': ('django.db.models.fields.BooleanField', [], {}),
            'pump_on': ('django.db.models.fields.BooleanField', [], {}),
            'south_call': ('django.db.models.fields.BooleanField', [], {}),
            'south_on': ('django.db.models.fields.BooleanField', [], {}),
            'sumplvl': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ditchdb']