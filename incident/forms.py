# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.files.uploadedfile import UploadedFile
from django.utils.translation import ugettext_lazy as _, ugettext as __
from incident.models import Incident
from ragendja.auth.models import UserTraits
from ragendja.forms import FormWithSets, FormSetField

class IncidentForm(forms.ModelForm):
    short_summary = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=30)),
        label=_(u'Public Summary'))
    description = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=2000)),
        label=_(u'Full Description'))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)),
        label=_(u'Email address'))
    date = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=30)),
        label=_(u'Incident Date'))
    time = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=30)),
        label=_(u'Incident Time'))
    category = forms.ChoiceField(choices=(('roadrage','Road Rage'),('crash','Crash'),('assault','Assault'),('other','Other')),
        widget=forms.Select(),
        label=_(u'Category'))
    location_lat = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=75)),
        label=_(u'Location latitude'))
    location_lng = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=75)),
        label=_(u'Location longitude'))

    def clean_short_summary(self):
        incident = Incident.get_by_key_name("key_"+self.cleaned_data['short_summary'].lower())
        if incident:
            raise forms.ValidationError(__(u'This summary was used in a previous incident. Please choose another.'))
        return self.cleaned_data['short_summary']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

    class Meta:
        model = Incident
