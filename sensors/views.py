from sensors.models import SensorData, LoRaGatewayData
from sensors.serializers import SensorDataSerializer, LoRaGatewayDataSerializer
from rest_framework import viewsets, status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_csv.renderers import CSVRenderer

#from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
#from rest_framework_csv.parsers import CSVParser
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import action

# define custom CSV headers when rendering
class SensorCSVRender(CSVRenderer):
    header = ['id', 'timestamp', 'relay_id', 'sensor_id',
              'sensor_type', 'units', 'data', 'longitude', 'latitude',
              'altitude', 'speed', 'climb']

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    #parser_classes = (JSONParser, FormParser, MultiPartParser, CSVParser,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, SensorCSVRender,)


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
