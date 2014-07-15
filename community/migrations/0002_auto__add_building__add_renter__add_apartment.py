# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Building'
        db.create_table(u'community_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('floors', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'community', ['Building'])

        # Adding model 'Renter'
        db.create_table(u'community_renter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apartment', to=orm['community.Apartment'])),
        ))
        db.send_create_signal(u'community', ['Renter'])

        # Adding M2M table for field complaints on 'Renter'
        m2m_table_name = db.shorten_name(u'community_renter_complaints')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('renter', models.ForeignKey(orm[u'community.renter'], null=False)),
            ('building', models.ForeignKey(orm[u'community.building'], null=False))
        ))
        db.create_unique(m2m_table_name, ['renter_id', 'building_id'])

        # Adding model 'Apartment'
        db.create_table(u'community_apartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('rooms', self.gf('django.db.models.fields.IntegerField')()),
            ('rent', self.gf('django.db.models.fields.IntegerField')()),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(related_name='building', to=orm['community.Building'])),
        ))
        db.send_create_signal(u'community', ['Apartment'])


    def backwards(self, orm):
        # Deleting model 'Building'
        db.delete_table(u'community_building')

        # Deleting model 'Renter'
        db.delete_table(u'community_renter')

        # Removing M2M table for field complaints on 'Renter'
        db.delete_table(db.shorten_name(u'community_renter_complaints'))

        # Deleting model 'Apartment'
        db.delete_table(u'community_apartment')


    models = {
        u'community.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'building'", 'to': u"orm['community.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'rent': ('django.db.models.fields.IntegerField', [], {}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        u'community.building': {
            'Meta': {'object_name': 'Building'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'floors': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'community.renter': {
            'Meta': {'object_name': 'Renter'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apartment'", 'to': u"orm['community.Apartment']"}),
            'complaints': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'building_complaints'", 'symmetrical': 'False', 'to': u"orm['community.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['community']