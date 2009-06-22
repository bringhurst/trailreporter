# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('incident.views',
    (r'^list/$', 'list_incidents'),
    (r'^create/$', 'add_incident'),
    (r'^show/(?P<key>.+)$', 'show_incident'),
    (r'^edit/(?P<key>.+)$', 'edit_incident'),
    (r'^delete/(?P<key>.+)$', 'delete_incident'),
)
