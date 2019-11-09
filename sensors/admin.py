from django.contrib import admin
from .models import *

admin.site.register(SensorDataLtBigSense)
admin.site.register(Sensor)
admin.site.register(SensorMetadata)
admin.site.register(SensorData)