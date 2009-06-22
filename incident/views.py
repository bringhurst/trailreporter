# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, \
    update_object
from google.appengine.ext import db
from mimetypes import guess_type
from incident.forms import IncidentForm
from incident.models import Incident
from ragendja.dbutils import get_object_or_404
from ragendja.template import render_to_response

def list_incidents(request):
    return object_list(request, Incident.all(), paginate_by=10)

def show_incident(request, key):
    return object_detail(request, Incident.all(), key)

def add_incident(request):
    return create_object(request, form_class=IncidentForm,
        post_save_redirect=reverse('incident.views.show_incident',
                                   kwargs=dict(key='%(key)s')))

def edit_incident(request, key):
    return update_object(request, object_id=key, form_class=IncidentForm)

def delete_incident(request, key):
    return delete_object(request, Incident, object_id=key,
        post_delete_redirect=reverse('incident.views.list_incidents'))
