#!/usr/bin/env python
# https://docs.djangoproject.com/en/2.2/ref/contrib/gis/serializers/
from django.core.serializers import serialize
from world.models import *

geojson = serialize('geojson', WorldBorder.objects.all(), geometry_field='mpoly', fields=('name',))

with open('worldborder.geojson', 'w') as f:
    f.write(geojson)
