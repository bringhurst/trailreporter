from google.appengine.ext import db

class Incident(db.Model):
    short_summary = db.StringProperty(required=True)
    description = db.StringProperty(multiline=True,required=True)
    email_address = db.EmailProperty(required=True)
    date = db.StringProperty(required=True)
    time = db.TimeProperty(required=True)
    category = db.StringProperty(required=True,choices=set(["Road Rage","Crash","Assault","Other"]))
    location_lat = db.StringProperty(required=True)
    location_lng = db.StringProperty(required=True)
    created_on = db.DateProperty(auto_now_add=1)
    created_by = db.UserProperty()

    def __str__(self):
        return '%s' %self.short_summary

    def get_absolute_url(self):
        return '/incident/%s/detail' % self.key()

