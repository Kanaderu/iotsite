from rest_framework import serializers
from external_api.models import DarkSkyDataPoint, DarkSkyDataBlock, DarkSkyAlerts, DarkSkyFlag, DarkSky

class DarkSkyDataPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = DarkSkyDataPoint
        fields = '__all__'

class DarkSkyDataBlockSerializer(serializers.ModelSerializer):
    data = DarkSkyDataPointSerializer(many=True)

    class Meta:
        model = DarkSkyDataBlock
        fields = ['data', 'summary', 'icon']

class DarkSkyDataAlertsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DarkSkyAlerts
        fields = '__all__'

class DarkSkyDataFlagSerializer(serializers.ModelSerializer):
    darksky_unavailable = serializers.BooleanField(required=False, source='darksky-unavailable')
    nearest_station = serializers.DecimalField(max_digits=7, decimal_places=4, required=False, source='nearest-station')

    class Meta:
        model = DarkSkyFlag
        fields = '__all__'

class DarkSkySerializer(serializers.ModelSerializer):
    currently = DarkSkyDataPointSerializer(required=False)
    minutely = DarkSkyDataBlockSerializer(required=False)
    hourly = DarkSkyDataBlockSerializer(required=False)
    daily = DarkSkyDataBlockSerializer(required=False)
    #alerts = DarkSkyDataAlertsSerializer(many=True)
    flags = DarkSkyDataFlagSerializer(required=False)

    class Meta:
        model = DarkSky
        fields = ['latitude', 'longitude', 'timezone', 'offset',
                  'currently', 'minutely', 'hourly', 'daily', 'flags']
                  #'currently', 'minutely', 'hourly', 'daily', 'alerts', 'flags']
