# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PoliticalBuy.ignore_post_save'
        db.add_column('fccpublicfiles_politicalbuy', 'ignore_post_save',
                      self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PoliticalBuy.ignore_post_save'
        db.delete_column('fccpublicfiles_politicalbuy', 'ignore_post_save')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'broadcasters.broadcaster': {
            'Meta': {'ordering': "('community_state', 'community_city', 'callsign')", 'object_name': 'Broadcaster'},
            'callsign': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'channel': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'community_city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'community_state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'dma_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'facility_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facility_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network_affiliate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nielsen_dma': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'doccloud.document': {
            'Meta': {'ordering': "['created_at']", 'object_name': 'Document'},
            'access_level': ('django.db.models.fields.CharField', [], {'default': "'private'", 'max_length': '32'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True', 'blank': 'True'}),
            'dc_properties': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doccloud.DocumentCloudProperties']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "('title',)", 'overwrite': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'doccloud.documentcloudproperties': {
            'Meta': {'object_name': 'DocumentCloudProperties'},
            'dc_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dc_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fccpublicfiles.genericpublicdocument': {
            'Meta': {'object_name': 'GenericPublicDocument'},
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_genericpublicdocument_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'broadcasters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['broadcasters.Broadcaster']", 'null': 'True', 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_genericpublicdocument_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'documentcloud_doc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doccloud.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_genericpublicdocument_updated'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'fccpublicfiles.organization': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organization'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['locations.Address']", 'null': 'True', 'blank': 'True'}),
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_organization_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_organization_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'employees': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fccpublicfiles.Person']", 'through': "orm['fccpublicfiles.Role']", 'symmetrical': 'False'}),
            'fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'organization_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'related_advertiser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fccpublicfiles.TV_Advertiser']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_organization_updated'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'fccpublicfiles.person': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Person'},
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_person_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_person_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_person_updated'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'fccpublicfiles.politicalbuy': {
            'Meta': {'object_name': 'PoliticalBuy'},
            'advertiser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'advertiser_politicalbuys'", 'null': 'True', 'to': "orm['fccpublicfiles.Organization']"}),
            'advertiser_signatory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fccpublicfiles.Person']", 'null': 'True', 'blank': 'True'}),
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_politicalbuy_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'bought_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mediabuyer_politicalbuys'", 'null': 'True', 'to': "orm['fccpublicfiles.Organization']"}),
            'broadcasters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['broadcasters.Broadcaster']", 'null': 'True', 'symmetrical': 'False'}),
            'candidate_type': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'community_state': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'contract_end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'contract_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'contract_start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_politicalbuy_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'data_entry_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dma_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'documentcloud_doc': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['doccloud.Document']", 'null': 'True'}),
            'fcc_folder_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignore_post_save': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_FCC_doc': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_invalid': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_summarized': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'lowest_unit_price': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'nielsen_dma': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'num_spots_raw': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'related_FCC_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraper.PDF_File']", 'null': 'True', 'blank': 'True'}),
            'total_spent_raw': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_politicalbuy_updated'", 'null': 'True', 'to': "orm['auth.User']"}),
            'uuid_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        'fccpublicfiles.politicalspot': {
            'Meta': {'object_name': 'PoliticalSpot'},
            'airing_days': ('weekday_field.fields.WeekdayField', [], {'max_length': '14', 'blank': 'True'}),
            'airing_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'airing_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_politicalspot_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'broadcast_length': ('timedelta.fields.TimedeltaField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_politicalspot_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fccpublicfiles.PoliticalBuy']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'num_spots': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preemptable': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'show_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'timeslot_begin': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'timeslot_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_politicalspot_updated'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'fccpublicfiles.role': {
            'Meta': {'object_name': 'Role'},
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_role_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_role_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fccpublicfiles.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fccpublicfiles.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fccpublicfiles_role_updated'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'fccpublicfiles.tv_advertiser': {
            'Meta': {'object_name': 'TV_Advertiser'},
            'ad_hawk_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'advertiser_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fecdata.Candidate']", 'null': 'True'}),
            'candidate_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'committee_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ftum_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ie_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_in_adhawk': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'num_broadcasters': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_buys': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_dmas': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_recent_broadcasters': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_recent_buys': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_recent_dmas': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_recent_state': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_states': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary committee'", 'null': 'True', 'to': "orm['fecdata.Committee']"}),
            'recent_amount_guess': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recent_amount_guess_high': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recent_amount_guess_low': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secondary_committees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'secondary committees'", 'null': 'True', 'to': "orm['fecdata.Committee']"}),
            'total_amount_guess': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_amount_guess_high': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_amount_guess_low': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'fccpublicfiles.tv_advertiser_alias': {
            'Meta': {'object_name': 'TV_Advertiser_Alias'},
            'advertiser_name_clean': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'advertiser_name_raw': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fccpublicfiles.TV_Advertiser']", 'null': 'True'})
        },
        'fecdata.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'campaign_com_fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'candidate_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'cycle': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'fec_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'seat_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state_address': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'state_race': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        'fecdata.committee': {
            'Meta': {'object_name': 'Committee'},
            'candidate_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'candidate_office': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True', 'blank': 'True'}),
            'connected_org_name': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'ctype': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'filing_frequency': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_group_cat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'is_hybrid': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_nonprofit': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_superpac': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'related_candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fecdata.Candidate']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'state_race': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street_1': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'street_2': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'tax_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'treasurer': ('django.db.models.fields.CharField', [], {'max_length': '38', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'locations.address': {
            'Meta': {'unique_together': "(('address1', 'address2', 'city', 'state', 'zipcode'),)", 'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'approved_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations_address_approved'", 'null': 'True', 'to': "orm['auth.User']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations_address_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations_address_updated'", 'null': 'True', 'to': "orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'scraper.folder': {
            'Meta': {'object_name': 'Folder'},
            'broadcaster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['broadcasters.Broadcaster']", 'null': 'True', 'blank': 'True'}),
            'callsign': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'facility_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'folder_class': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'folder_name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '511'}),
            'related_candidate_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'related_pac_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'scrape_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'scraper.pdf_file': {
            'Meta': {'object_name': 'PDF_File'},
            'ad_type': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'callsign': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'community_state': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'dc_slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dc_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dma_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'facility_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'federal_district': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'federal_office': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraper.Folder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_document_cloud': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'nielsen_dma': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'raw_name_guess': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'raw_url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '511'}),
            'related_candidate_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'related_pac_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'upload_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fccpublicfiles']