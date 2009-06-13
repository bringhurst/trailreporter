from django.http import HttpResponse, HttpResponseRedirect
from trailreporter.incident import models
import bforms
from django.shortcuts import render_to_response

def render(template, payload):
    payload['recents'] = models.Incident.all().order('-created_on').fetch(5)
    return render_to_response(template, payload)

def index(request):
    incidents = models.Incident.all().order('-created_on').fetch(20)
    payload = dict(incidents = incidents)
    return render('index.html', payload)

def create(request):
    if request.method == 'GET':
        incidentform = bforms.IncidentForm()
    if request.method == 'POST':
        incidentform = bforms.IncidentForm(request.POST)
        if incidentform.is_valid():
            incident = incidentform.save()
            return HttpResponseRedirect(incident.get_absolute_url())
    payload = dict(incidentform=incidentform)
    return render('incident_create.html', payload)

def detail(request, incident_key):
    incident = models.Incident.get(incident_key)
    payload = dict(incident = incident)
    return render('incident_detail.html', payload)

def edit(request, incident_key):
    incident = models.Incident.get(incident_key)
    if request.method == 'POST':
        # TODO: implement edit logic here
        return HttpResponseRedirect('/')
    payload = dict(incident = incident)
    return render('incident_edit.html', payload)

def delete(request, incident_key):
    incident = models.Incident.get(incident_key)
    payload = dict(incident = incident)
    models.Incident.delete(incident)
    return render('incident_delete.html', payload)

