# -*- coding: utf-8 -*-
from django.db.models import permalink
from google.appengine.ext import db

class Incident(db.Model):
    short_summary = db.StringProperty(required=True)
    description = db.StringProperty(multiline=True,required=True)
    email = db.EmailProperty(required=True)
    date = db.StringProperty(required=True)
    time = db.StringProperty(required=True)
    category = db.StringProperty(required=True)
    location_lat = db.StringProperty(required=True)
    location_lng = db.StringProperty(required=True)

    def __unicode__(self):
        return '%s' % self.short_summary

    @permalink
    def get_absolute_url(self):
        return ('incident.views.show_incident', (), {'key': self.key()})
