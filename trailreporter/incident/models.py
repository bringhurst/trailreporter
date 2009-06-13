from google.appengine.ext import db

class Incident(db.Model):
    short_summary = db.StringProperty()
    description = db.StringProperty()
    email_address = db.StringProperty()
    incident_datetime = db.DateTimeProperty()
    category = db.StringProperty()
    latitude = db.StringProperty()
    longitude = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add = 1)
    created_by = db.UserProperty()

    def __str__(self):
        return '%s' %self.short_summary

    def get_absolute_url(self):
        return '/incident/%s/detail' % self.key()

