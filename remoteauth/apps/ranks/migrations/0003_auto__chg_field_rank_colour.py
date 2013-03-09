# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Rank.colour'
        db.alter_column('ranks_rank', 'colour', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Rank.colour'
        db.alter_column('ranks_rank', 'colour', self.gf('django.db.models.fields.IntegerField')(max_length=1))

    models = {
        'ranks.rank': {
            'Meta': {'ordering': "('price', 'name')", 'object_name': 'Rank'},
            'colour': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'max_length': '100'})
        }
    }

    complete_apps = ['ranks']