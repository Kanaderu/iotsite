import graphene
import json
from django.contrib.gis.db import models
from graphene_django.types import DjangoObjectType
from graphene_django.converter import convert_django_field
from .models import Sensor, SensorData


class GeoJSON(graphene.Scalar):

    @classmethod
    def serialize(cls, value):
        return json.loads(value.geojson)


@convert_django_field.register(models.GeometryField)
def convert_field_to_geojson(field, registry=None):
    return graphene.Field(
        GeoJSON,
        description=field.help_text,
        required=not field.null)


class SensorType(DjangoObjectType):
    class Meta:
        model = Sensor


class SensorDataType(DjangoObjectType):
    class Meta:
        model = SensorData


class Query(object):
    sensors = graphene.List(SensorType)
    sensor_data = graphene.List(SensorDataType)

    def resolve_sensors(self, info, **kwargs):
        return Sensor.objects.all()

    def resolve_sensor_data(self, info, **kwargs):
        return SensorData.objects.select_related('sensor').all()
