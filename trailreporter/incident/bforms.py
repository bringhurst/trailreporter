from django import newforms as forms
import models
from google.appengine.ext.db import djangoforms

class IncidentForm(djangoforms.ModelForm):
    class Meta:
        model = models.Incident
        exclude = ['created_by']

