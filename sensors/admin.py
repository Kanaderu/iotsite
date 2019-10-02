from django.contrib import admin
from .models import SensorData, LoRaGateway, LoRaGatewayMetadata, LoRaGatewayData, LoRaGatewayPayloadFields

admin.site.register(SensorData)
admin.site.register(LoRaGateway)
admin.site.register(LoRaGatewayMetadata)
admin.site.register(LoRaGatewayData)
admin.site.register(LoRaGatewayPayloadFields)