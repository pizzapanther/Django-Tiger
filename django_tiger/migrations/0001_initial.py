# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CreditCard'
        db.create_table('django_tiger_creditcard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last4', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('ctype', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('exp_month', self.gf('django.db.models.fields.IntegerField')()),
            ('exp_year', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('django_tiger', ['CreditCard'])

        # Adding model 'Subscription'
        db.create_table('django_tiger_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_tiger.CreditCard'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('customer_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('plan_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('django_tiger', ['Subscription'])


    def backwards(self, orm):
        # Deleting model 'CreditCard'
        db.delete_table('django_tiger_creditcard')

        # Deleting model 'Subscription'
        db.delete_table('django_tiger_subscription')


    models = {
        'django_tiger.creditcard': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'CreditCard'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctype': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'exp_month': ('django.db.models.fields.IntegerField', [], {}),
            'exp_year': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'django_tiger.subscription': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Subscription'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_tiger.CreditCard']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['django_tiger']