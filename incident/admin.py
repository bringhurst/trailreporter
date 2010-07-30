from django.contrib import admin
from incident.models import Incident

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('short_summary','date')

admin.site.register(Incident, IncidentAdmin)
