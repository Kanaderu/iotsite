from sensors.models import *
from sensors.serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins, status
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_csv.renderers import CSVRenderer

#from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
#from rest_framework_csv.parsers import CSVParser
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import action


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = '__all__'
    search_fields = ['sensor', 'sensor_id']
    ordering_fields = '__all__'


class LoRaGatewaySensorViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.ViewSet):
    serializer_class = LoRaGatewaySensorSerializer
    pagination_class = PageNumberPagination

    def list(self, request):
        queryset = Sensor.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sensor.objects.all()
        sensor = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(sensor)
        return Response(serializer.data)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer_context(self):
        return {'request': self.request}


class FeatherSensorViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.ViewSet):
    serializer_class = FeatherSensorSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.pagination_class().paginate_queryset(queryset, request)
        '''
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        '''
        '''
        queryset = Sensor.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        '''
        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sensor.objects.all()
        sensor = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(sensor)
        return Response(serializer.data)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return Sensor.objects.all()


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


class FeatherDataV2View(viewsets.ModelViewSet):
    queryset = FeatherDataV2.objects.all()
    serializer_class = FeatherDataV2Serializer
    filterset_fields = '__all__'
    search_fields = ['dev_id', 'metadata', 'data']
    ordering_fields = '__all__'
'''