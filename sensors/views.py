from sensors.serializers import *
from rest_framework import viewsets, permissions#, mixins, status
from django.shortcuts import render#, get_object_or_404
from django.utils.safestring import mark_safe
import json
#from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
#from rest_framework_csv.renderers import CSVRenderer

#from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
#from rest_framework_csv.parsers import CSVParser
#from django.urls import reverse
#from rest_framework.response import Response
#from rest_framework.decorators import action
#from rest_framework import generics
#from django.http import Http404

from djgeojson.views import GeoJSONLayerView


# modify queryset for the most recent data across all sensors
class LatestSensorGeoJSONLayerView(GeoJSONLayerView):
    def get_queryset(self):
        items = set()
        for sensor_type in Sensor.SENSOR_CHOICES:
            latest_item = Sensor.objects.filter(sensor=sensor_type[0]).order_by('-created').first()
            if latest_item is not None:
                items.add(latest_item.pk)

        context = Sensor.objects.filter(pk__in=items)
        return context


class SensorViewSet(viewsets.ModelViewSet):
    """
    Sensor API
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = '__all__'
    search_fields = ['sensor', 'sensor_id']
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class LoRaGatewaySensorViewSet(SensorViewSet):
    serializer_class = LoRaGatewaySensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class FeatherSensorViewSet(SensorViewSet):
    serializer_class = FeatherSensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


def live_index(request):
    return render(request, 'sensors/index.html', {})


def live_room(request, sensors):
    return render(request, 'sensors/room.html', {
        'sensors_json': mark_safe(json.dumps(sensors))
    })


'''
# define custom CSV headers when rendering
class SensorCSVRender(CSVRenderer):
    header = ['id', 'timestamp', 'relay_id', 'sensor_id',
              'sensor_type', 'units', 'data', 'longitude', 'latitude',
              'altitude', 'speed', 'climb']

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorDataLtBigSense.objects.all()
    serializer_class = SensorDataSerializer
    #parser_classes = (JSONParser, FormParser, MultiPartParser, CSVParser,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, SensorCSVRender,)
    filterset_fields = '__all__'
    search_fields = ['timestamp', 'relay_id', 'sensor_id', 'sensor_type', 'units', 'data', 'longitude', 'latitude', 'altitude', 'speed', 'climb']
    ordering_fields = '__all__'

    @action(methods=['POST'], detail=False)
    def bulk_post(self, request, *args, **kwargs):
        """
        Try out this view with the following curl command:
        curl -X POST http://localhost:8000/api/sensors/bulk_post/ \
            -d "package_id,timestamp,relay_id,sensor_id,sensor_type,units,data
                3513,2018-11-03T15:15:00-04:00,KUGreenRoof,FF08A9B01604,Temperature,63.0500,F
                3514,2018-11-03T15:16:00-04:00,KUGreenRoof,FF08A9B01604,Temperature,64.0500,F" \
            -H "Content-type: text/csv" \
            -H "Accept: text/csv"
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_303_SEE_OTHER, headers={'Location': reverse('sensordata-list')})


class LoRaGatewayDataView(viewsets.ModelViewSet):
    queryset = LoRaGatewayData.objects.all()
    serializer_class = LoRaGatewayDataSerializer
    filterset_fields = '__all__'
    search_fields = ['app_id', 'dev_id', 'hardware_serial', 'port', 'counter', 'payload_raw', 'downlink_url',
                     'payload_fields__b', 'payload_fields__sm1', 'payload_fields__sm2', 'payload_fields__sm3',
                     'payload_fields__sm4', 'payload_fields__t1', 'payload_fields__t2', 'metadata__time',
                     'metadata__frequency', 'metadata__modulation', 'metadata__data_rate', 'metadata__coding_rate',
                     'metadata__gateways__gtw_id', 'metadata__gateways__gtw_trusted', 'metadata__gateways__timestamp',
                     'metadata__gateways__time', 'metadata__gateways__channel', 'metadata__gateways__rssi',
                     'metadata__gateways__snr', 'metadata__gateways__rf_chain']
    ordering_fields = '__all__'


class FeatherDataView(viewsets.ModelViewSet):
    queryset = FeatherDataV2.objects.all()
    serializer_class = FeatherDataV2Serializer
    filterset_fields = '__all__'
    search_fields = ['dev_id', 'metadata', 'data']
    ordering_fields = '__all__'
'''
