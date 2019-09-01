from sensors.models import SensorData
from sensors.serializers import SensorDataSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_csv.renderers import CSVRenderer

# define custom CSV headers when rendering
class SensorCSVRender(CSVRenderer):
    header = ['package_id', 'timestamp', 'relay_id', 'sensor_id',
              'sensor_type', 'units', 'data', 'longitude', 'latitude',
              'altitude', 'speed', 'climb']

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    #parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, SensorCSVRender,)

