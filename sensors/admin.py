from django.contrib import admin
from .models import *

admin.site.register(SensorDataLtBigSense)
admin.site.register(LoRaGateway)
admin.site.register(LoRaGatewayMetadata)
admin.site.register(LoRaGatewayData)
admin.site.register(LoRaGatewayPayloadFields)
admin.site.register(FeatherDataV2)
admin.site.register(FeatherSensorDataV2)
admin.site.register(FeatherMetadataV2)
