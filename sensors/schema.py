import graphene
from graphene_django.types import DjangoObjectType
import graphql_geojson
from .models import Sensor, SensorData#, SensorMetadata


class SensorType(DjangoObjectType):
    class Meta:
        model = Sensor


'''
class SensorMetadataType(DjangoObjectType):
    class Meta:
        model = SensorMetadata
        geojson_field = 'coordinates'
'''


class SensorDataType(DjangoObjectType):
    class Meta:
        model = SensorData


class Query(object):
    all_sensors = graphene.List(SensorType)
    #all_sensor_metadata = graphene.List(SensorMetadataType)
    all_sensor_data = graphene.List(SensorDataType)

    def resolve_all_sensors(self, info, **kwargs):
        return Sensor.objects.all()

    #def resolve_all_sensor_metadata(self, info, **kwargs):
    #    return SensorMetadata.objects.select_related('sensor').all()

    def resolve_all_sensor_data(self, info, **kwargs):
        return SensorData.objects.select_related('sensor').all()
