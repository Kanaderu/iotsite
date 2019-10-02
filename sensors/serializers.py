from rest_framework import serializers
from sensors.models import *


class SensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ['id', 'timestamp', 'relay_id', 'sensor_id',
                  'sensor_type', 'units', 'data', 'longitude', 'latitude',
                  'altitude', 'speed', 'climb']


class LoRaGatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = LoRaGateway
        fields = ['gtw_id', 'gtw_trusted', 'timestamp', 'time', 'channel',
                  'rssi', 'snr', 'rf_chain', 'latitude', 'longitude']


class LoRaGatewayMetadataSerializer(serializers.ModelSerializer):

    gateways = LoRaGatewaySerializer(many=True)

    class Meta:
        model = LoRaGatewayMetadata
        fields = ['time', 'frequency', 'modulation', 'data_rate', 'coding_rate', 'gateways']


class LoRaGatewayPayloadFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoRaGatewayPayloadFields
        fields = ['b', 'sm1', 'sm2', 'sm3', 'sm4']


class LoRaGatewayDataSerializer(serializers.ModelSerializer):

    payload_fields = LoRaGatewayPayloadFieldsSerializer(required=True)
    metadata = LoRaGatewayMetadataSerializer(required=True)

    class Meta:
        model = LoRaGatewayData
        fields = ['app_id', 'dev_id', 'hardware_serial', 'port', 'counter',
                  'payload_raw', 'payload_fields', 'metadata', 'downlink_url']

    def create(self, validated_data):
        payload_data = validated_data.pop('payload_fields')
        metadata_data = validated_data.pop('metadata')
        gateways_data = metadata_data.pop('gateways')

        instance = LoRaGatewayData.objects.create(**validated_data)
        LoRaGatewayPayloadFields.objects.create(gateway_data=instance, **payload_data)
        meta_instance = LoRaGatewayMetadata.objects.create(gateway_data=instance, **metadata_data)

        for gateway_data in gateways_data:
            LoRaGateway.objects.create(metadata=meta_instance, **gateway_data)

        return instance
