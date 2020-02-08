from rest_framework import serializers
from django.contrib.gis.geos import Point
from sensors.models import *


class SensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ['data_id', 'type', 'data', 'units']


class SensorSerializer(serializers.ModelSerializer):
    data = SensorDataSerializer(many=True, required=True)
    coordinates = serializers.ListField()

    class Meta:
        model = Sensor
        fields = ['sensor', 'sensor_id', 'timestamp', 'coordinates', 'data']


class LoRaGatewaySensorSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        return SensorSerializer().to_representation(obj)

    def to_internal_value(self, data):
        sensor_id = data.get('dev_id')
        metadata = data.get('metadata')
        timestamp = metadata.get('time')
        gateways_data = metadata.get('gateways')

        if not isinstance(gateways_data, list):
            raise serializers.ValidationError({
                'gateways': 'This field is required.'
            })

        gateways = []
        for item in gateways_data:
            if item.get('latitude') is None:
                raise serializers.ValidationError('latitude is required')
            if item.get('longitude') is None:
                raise serializers.ValidationError('longitude is required')
            gateways.append({'latitude': item.get('latitude'),
                             'longitude': item.get('longitude')})

        latitude = gateways[0]['latitude']
        longitude = gateways[0]['longitude']

        payload_fields = data.get('payload_fields')
        b = payload_fields.get('b')
        sm1 = payload_fields.get('sm1')
        sm2 = payload_fields.get('sm2')
        sm3 = payload_fields.get('sm3')
        sm4 = payload_fields.get('sm4')
        t1 = payload_fields.get('t1')
        t2 = payload_fields.get('t2')

        if not sensor_id:
            raise serializers.ValidationError({
                'sensor_id': 'This field is required.'
            })
        if not timestamp:
            raise serializers.ValidationError({
                'timestamp': 'This field is required.'
            })
        if not b:
            raise serializers.ValidationError({
                'b': 'This field is required.'
            })
        if not sm1:
            raise serializers.ValidationError({
                'sm1': 'This field is required.'
            })
        if not sm2:
            raise serializers.ValidationError({
                'sm2': 'This field is required.'
            })
        if not sm3:
            raise serializers.ValidationError({
                'sm3': 'This field is required.'
            })
        if not sm4:
            raise serializers.ValidationError({
                'sm4': 'This field is required.'
            })
        if not t1:
            raise serializers.ValidationError({
                't1': 'This field is required.'
            })
        if not t2:
            raise serializers.ValidationError({
                't2': 'This field is required.'
            })

        return {
            'sensor_id': sensor_id,
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude,
            'b': b,
            'sm1': sm1,
            'sm2': sm2,
            'sm3': sm3,
            'sm4': sm4,
            't1': t1,
            't2': t2,
        }

    def create(self, validated_data):
        instance = Sensor.objects.create(sensor='LG', sensor_id=validated_data['sensor_id'],
                                         coordinates=Point(x=validated_data['longitude'], y=validated_data['latitude'], srid=4326),
                                         timestamp=validated_data['timestamp'])
        SensorData.objects.create(sensor=instance, data_id='b', data=validated_data['b'])
        SensorData.objects.create(sensor=instance, data_id='sm1', data=validated_data['sm1'])
        SensorData.objects.create(sensor=instance, data_id='sm2', data=validated_data['sm2'])
        SensorData.objects.create(sensor=instance, data_id='sm3', data=validated_data['sm3'])
        SensorData.objects.create(sensor=instance, data_id='sm4', data=validated_data['sm4'])
        SensorData.objects.create(sensor=instance, data_id='t1', data=validated_data['t1'])
        SensorData.objects.create(sensor=instance, data_id='t2', data=validated_data['t2'])

        return instance


class FeatherSensorSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        return SensorSerializer().to_representation(obj)

    def to_internal_value(self, data):
        dev_id = data['dev_id']
        metadata = data['metadata']
        latitude = metadata['latitude']
        longitude = metadata['longitude']
        timestamp = metadata['time']

        data_list = data['data']
        if not isinstance(data_list, list):
            raise serializers.ValidationError({
                'data': 'This field is required.'
            })

        sensor_data = []
        for item in data_list:
            if item['sensor_id'] is None:
                raise serializers.ValidationError('sensor_id is required')
            if item['sensor_type'] is None:
                raise serializers.ValidationError('sensor_type is required')
            if item['sensor_data'] is None:
                raise serializers.ValidationError('sensor_data is required')
            if item['sensor_units'] is None:
                raise serializers.ValidationError('sensor_units is required')
            sensor_data.insert(0, {'data_id': item['sensor_id'],
                                 'type': item['sensor_type'],
                                 'data': item['sensor_data'],
                                 'units': item['sensor_units'],})

        if not dev_id:
            raise serializers.ValidationError({
                'dev_id': 'This field is required.'
            })
        if not timestamp:
            raise serializers.ValidationError({
                'timestamp': 'This field is required.'
            })
        if not latitude:
            raise serializers.ValidationError({
                'latitude': 'This field is required.'
            })
        if not longitude:
            raise serializers.ValidationError({
                'longitude': 'This field is required.'
            })

        return {
            'sensor_id': dev_id,
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude,
            'data': sensor_data,
        }

    def create(self, validated_data):
        instance = Sensor.objects.create(sensor='F', sensor_id=validated_data['sensor_id'],
                                         coordinates=Point(x=validated_data['longitude'], y=validated_data['latitude'], srid=4326),
                                         timestamp=validated_data['timestamp'])
        for item in validated_data['data']:
            SensorData.objects.create(sensor=instance, data_id=item['data_id'], type=item['type'],
                                      data=item['data'], units=item['units'])

        return instance


'''
class MobileAppSensorSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        return SensorSerializer().to_representation(obj)

    def to_internal_value(self, data):
        dev_id = data['dev_id']
        metadata = data['metadata']
        latitude = metadata['latitude']
        longitude = metadata['longitude']
        timestamp = metadata['time']

        data_list = data['data']
        if not isinstance(data_list, list):
            raise serializers.ValidationError({
                'data': 'This field is required.'
            })

        sensor_data = []
        for item in data_list:
            if item['sensor_id'] is None:
                raise serializers.ValidationError('sensor_id is required')
            if item['sensor_type'] is None:
                raise serializers.ValidationError('sensor_type is required')
            if item['sensor_data'] is None:
                raise serializers.ValidationError('sensor_data is required')
            if item['sensor_units'] is None:
                raise serializers.ValidationError('sensor_units is required')
            sensor_data.insert(0, {'data_id': item['sensor_id'],
                                 'type': item['sensor_type'],
                                 'data': item['sensor_data'],
                                 'units': item['sensor_units'],})

        if not dev_id:
            raise serializers.ValidationError({
                'dev_id': 'This field is required.'
            })
        if not timestamp:
            raise serializers.ValidationError({
                'timestamp': 'This field is required.'
            })
        if not latitude:
            raise serializers.ValidationError({
                'latitude': 'This field is required.'
            })
        if not longitude:
            raise serializers.ValidationError({
                'longitude': 'This field is required.'
            })

        return {
            'sensor_id': dev_id,
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude,
            'data': sensor_data,
        }

    def create(self, validated_data):
        instance = Sensor.objects.create(sensor='M', sensor_id=validated_data['sensor_id'])
        SensorMetadata.objects.create(sensor=instance,
                                      coordinates=Point(x=validated_data['longitude'], y=validated_data['latitude'], srid=4326),
                                      timestamp=validated_data['timestamp'])
        for item in validated_data['data']:
            SensorData.objects.create(sensor=instance, data_id=item['data_id'], type=item['type'],
                                      data=item['data'], units=item['units'])

        return instance
'''
