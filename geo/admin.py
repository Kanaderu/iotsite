from django.contrib.gis import admin
from .models import *

#admin.site.register(WorldBorder) # NASA Layer
#admin.site.register(WorldBorder, admin.GeoModelAdmin) # Vector Map Level 0
admin.site.register(WorldBorder, admin.OSMGeoAdmin) # Open Street Maps
