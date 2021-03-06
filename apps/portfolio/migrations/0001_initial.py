# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'portfolio_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('src', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('src_small', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'portfolio', ['Image'])

        # Adding model 'Gallery'
        db.create_table(u'portfolio_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ratio', self.gf('django.db.models.fields.SmallIntegerField')(max_length=2, null=True, blank=True)),
            ('width_prev', self.gf('django.db.models.fields.IntegerField')(max_length=11, null=True, blank=True)),
            ('height_prev', self.gf('django.db.models.fields.IntegerField')(max_length=11, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(max_length=11, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(max_length=11, null=True, blank=True)),
            ('main_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='main_image', null=True, to=orm['portfolio.Image'])),
        ))
        db.send_create_signal(u'portfolio', ['Gallery'])

        # Adding M2M table for field images on 'Gallery'
        db.create_table(u'portfolio_gallery_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm[u'portfolio.gallery'], null=False)),
            ('image', models.ForeignKey(orm[u'portfolio.image'], null=False))
        ))
        db.create_unique(u'portfolio_gallery_images', ['gallery_id', 'image_id'])

        # Adding model 'Seo'
        db.create_table(u'portfolio_seo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'portfolio', ['Seo'])

        # Adding model 'Item'
        db.create_table(u'portfolio_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('gallery_is_item', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('dd_creation', self.gf('django.db.models.fields.DateTimeField')()),
            ('count_views', self.gf('django.db.models.fields.IntegerField')(max_length=11, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(max_length=11, blank=True)),
            ('seo', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['portfolio.Seo'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'portfolio', ['Item'])

        # Adding M2M table for field gallery on 'Item'
        db.create_table(u'portfolio_item_gallery', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'portfolio.item'], null=False)),
            ('gallery', models.ForeignKey(orm[u'portfolio.gallery'], null=False))
        ))
        db.create_unique(u'portfolio_item_gallery', ['item_id', 'gallery_id'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'portfolio_image')

        # Deleting model 'Gallery'
        db.delete_table(u'portfolio_gallery')

        # Removing M2M table for field images on 'Gallery'
        db.delete_table('portfolio_gallery_images')

        # Deleting model 'Seo'
        db.delete_table(u'portfolio_seo')

        # Deleting model 'Item'
        db.delete_table(u'portfolio_item')

        # Removing M2M table for field gallery on 'Item'
        db.delete_table('portfolio_item_gallery')


    models = {
        u'portfolio.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'height': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'height_prev': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'images'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['portfolio.Image']"}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_image'", 'null': 'True', 'to': u"orm['portfolio.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ratio': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'width_prev': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'src_small': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'count_views': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'blank': 'True'}),
            'dd_creation': ('django.db.models.fields.DateTimeField', [], {}),
            'gallery': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Gallery']", 'null': 'True', 'blank': 'True'}),
            'gallery_is_item': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'blank': 'True'}),
            'seo': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['portfolio.Seo']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'portfolio.seo': {
            'Meta': {'object_name': 'Seo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']