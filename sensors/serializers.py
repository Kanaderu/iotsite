from rest_framework import serializers
from sensors.models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ['id', 'timestamp', 'relay_id', 'sensor_id',
                  'sensor_type', 'units', 'data', 'longitude', 'latitude',
                  'altitude', 'speed', 'climb']
