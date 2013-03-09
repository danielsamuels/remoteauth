# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rank.description'
        db.add_column('ranks_rank', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rank.description'
        db.delete_column('ranks_rank', 'description')


    models = {
        'ranks.rank': {
            'Meta': {'ordering': "('price', 'name')", 'object_name': 'Rank'},
            'colour': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'})
        }
    }

    complete_apps = ['ranks']