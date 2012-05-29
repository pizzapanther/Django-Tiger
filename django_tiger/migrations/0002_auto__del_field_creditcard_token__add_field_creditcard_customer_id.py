# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CreditCard.token'
        db.delete_column('django_tiger_creditcard', 'token')

        # Adding field 'CreditCard.customer_id'
        db.add_column('django_tiger_creditcard', 'customer_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CreditCard.token'
        raise RuntimeError("Cannot reverse this migration. 'CreditCard.token' and its values cannot be restored.")
        # Deleting field 'CreditCard.customer_id'
        db.delete_column('django_tiger_creditcard', 'customer_id')


    models = {
        'django_tiger.creditcard': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'CreditCard'},
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