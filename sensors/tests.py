from django.test import TestCase

# Create your tests here.

import io
from rest_framework.parsers import JSONParser
from .serializers import *


def test_LoRaSerializer():
    json = b"""
    {
        "app_id":"dayton-engineering-and-geology",
        "dev_id":"180291",
        "hardware_serial":"000DB5390864367B",
        "port":2,
        "counter":4555,
        "payload_raw":"0oCH/////w==",
        "payload_fields":{
            "b":4.2,
            "sm1":255,
            "sm2":255,
            "sm3":255,
            "sm4":255,
            "t1":28,
            "t2":35
        },
        "metadata":{
            "time":"2019-09-29T17:17:03.147714091Z",
            "frequency":904.9,
            "modulation":"LORA",
            "data_rate":"SF10BW125",
            "coding_rate":"4/5",
            "gateways":[
                {
                    "gtw_id":"rg1xx294cb6",
                    "gtw_trusted":true,
                    "timestamp":10479492,
                    "time":"",
                    "channel":5,
                    "rssi":-58,
                    "snr":9.25,
                    "rf_chain":1,
                    "latitude":39.741287,
                    "longitude":-84.18488
                }
            ]
        },
        "downlink_url":"https://integrations.thethingsnetwork.org/ttn-us-west/api/v2/down/dayton-engineering-and-geology/webhook_test?key=ttn-account-v2.kY1MRQUoGICp7C9CAEvhEdGklPVWW-ztIiU0aVRLxno"
    }
    """
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    print(data)

    metadata_data = data.pop('metadata')
    gateway_data = metadata_data.pop('gateways')
    payload_fields_data = data.pop('payload_fields')

    serializer = LoRaGatewaySensorSerializer(data=data)
    print('VALID' if serializer.is_valid() else 'NOT VALID')
    print(serializer.validated_data)

    metadata_serializer = LoRaGatewayMetadataSerializer(data=metadata_data)
    print('VALID' if metadata_serializer.is_valid() else 'NOT VALID')
    print(metadata_serializer.validated_data)

    #print(metadata_serializer.validated_data['time'])

    gateway_serializer = LoRaGatewaySerializer(data=gateway_data)
    print('VALID' if gateway_serializer.is_valid() else 'NOT VALID')
    print(gateway_serializer.validated_data)

    payload_fields_serializer = LoRaGatewayPayloadFieldsSerializer(data=payload_fields_data)
    print('VALID' if payload_fields_serializer.is_valid() else 'NOT VALID')
    print(payload_fields_serializer.validated_data)

    print(payload_fields_serializer.validated_data['b'])
    #Sensor.objects.create(sensor='LG', sensor_id=)


def save_LoRaSerializer():
    json = b"""
    {
        "app_id":"dayton-engineering-and-geology",
        "dev_id":"180291",
        "hardware_serial":"000DB5390864367B",
        "port":2,
        "counter":4555,
        "payload_raw":"0oCH/////w==",
        "payload_fields":{
            "b":4.2,
            "sm1":255,
            "sm2":255,
            "sm3":255,
            "sm4":255,
            "t1":28,
            "t2":35
        },
        "metadata":{
            "time":"2019-09-29T17:17:03.147714091Z",
            "frequency":904.9,
            "modulation":"LORA",
            "data_rate":"SF10BW125",
            "coding_rate":"4/5",
            "gateways":[
                {
                    "gtw_id":"rg1xx294cb6",
                    "gtw_trusted":true,
                    "timestamp":10479492,
                    "time":"",
                    "channel":5,
                    "rssi":-58,
                    "snr":9.25,
                    "rf_chain":1,
                    "latitude":39.741287,
                    "longitude":-84.18488
                }
            ]
        },
        "downlink_url":"https://integrations.thethingsnetwork.org/ttn-us-west/api/v2/down/dayton-engineering-and-geology/webhook_test?key=ttn-account-v2.kY1MRQUoGICp7C9CAEvhEdGklPVWW-ztIiU0aVRLxno"
    }
    """
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    print(data)

    serializer = LoRaGatewaySensorSerializer(data=data)
    print('VALID' if serializer.is_valid() else 'NOT VALID {}'.format(serializer.error_messages))
    serializer.save()