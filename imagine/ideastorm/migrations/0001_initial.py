# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idea'
        db.create_table(u'ideastorm_idea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ideastorm', ['Idea'])

        # Adding model 'IdeaComment'
        db.create_table(u'ideastorm_ideacomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('idea', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['ideastorm.Idea'])),
        ))
        db.send_create_signal(u'ideastorm', ['IdeaComment'])


    def backwards(self, orm):
        # Deleting model 'Idea'
        db.delete_table(u'ideastorm_idea')

        # Deleting model 'IdeaComment'
        db.delete_table(u'ideastorm_ideacomment')


    models = {
        u'ideastorm.idea': {
            'Meta': {'object_name': 'Idea'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'ideastorm.ideacomment': {
            'Meta': {'object_name': 'IdeaComment'},
            'comment_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['ideastorm.Idea']"})
        }
    }

    complete_apps = ['ideastorm']