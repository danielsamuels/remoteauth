# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rank.price'
        db.add_column('ranks_rank', 'price',
                      self.gf('django.db.models.fields.FloatField')(default=0.0, max_length=100),
                      keep_default=False)

        # Adding field 'Rank.colour'
        db.add_column('ranks_rank', 'colour',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rank.price'
        db.delete_column('ranks_rank', 'price')

        # Deleting field 'Rank.colour'
        db.delete_column('ranks_rank', 'colour')


    models = {
        'ranks.rank': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Rank'},
            'colour': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'max_length': '100'})
        }
    }

    complete_apps = ['ranks']