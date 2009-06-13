from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'trailreporter.incident.views.index'),
    (r'^create/$', 'trailreporter.incident.views.create'),
    (r'^admin/$', 'trailreporter.incident.views.admin'),
    (r'^incident/(?P<incident_key>[^\.^/]+)/detail[/]?$', 'trailreporter.incident.views.detail'),
    (r'^incident/(?P<incident_key>[^\.^/]+)/delete[/]?$', 'trailreporter.incident.views.delete'),
    (r'^incident/(?P<incident_key>[^\.^/]+)/edit[/]?$', 'trailreporter.incident.views.edit'),
)

