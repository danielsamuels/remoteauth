# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DescriptionLine'
        db.create_table('ranks_descriptionline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ranks.Rank'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('ranks', ['DescriptionLine'])

        # Deleting field 'Rank.description'
        db.delete_column('ranks_rank', 'description')


    def backwards(self, orm):
        # Deleting model 'DescriptionLine'
        db.delete_table('ranks_descriptionline')

        # Adding field 'Rank.description'
        db.add_column('ranks_rank', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)


    models = {
        'ranks.descriptionline': {
            'Meta': {'object_name': 'DescriptionLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ranks.Rank']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'ranks.rank': {
            'Meta': {'ordering': "('price', 'name')", 'object_name': 'Rank'},
            'colour': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'purchasable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['ranks']