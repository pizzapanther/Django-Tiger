# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Charge'
        db.create_table('django_tiger_charge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('charge_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_tiger.CreditCard'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('refunded', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('django_tiger', ['Charge'])

        # Adding field 'CreditCard.active'
        db.add_column('django_tiger_creditcard', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Charge'
        db.delete_table('django_tiger_charge')

        # Deleting field 'CreditCard.active'
        db.delete_column('django_tiger_creditcard', 'active')


    models = {
        'django_tiger.charge': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Charge'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_tiger.CreditCard']"}),
            'charge_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refunded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'django_tiger.creditcard': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'CreditCard'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctype': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exp_month': ('django.db.models.fields.IntegerField', [], {}),
            'exp_year': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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