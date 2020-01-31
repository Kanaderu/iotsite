from django.urls import path
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import WorldBorder, LINKStation
from sensors.views import LatestSensorGeoJSONLayerView

from sensors.models import Sensor, SensorMetadata

from .views import GeoJSONLinkStations

urlpatterns = [
    path('linkstations.geojson', GeoJSONLinkStations, name='linkstations'),
    path('worldpoints.geojson', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='lat_lon', properties=('name',)), name='worldpoints'),
    path('worldborders.geojson', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='mpoly', properties=('name',)), name='worldborders'),
    #path('linkstations.geojson', GeoJSONLayerView.as_view(model=LINKStation, properties=('name',)), name='linkstations'),

    path('sensor.geojson', GeoJSONLayerView.as_view(model=SensorMetadata, geometry_field='coordinates',
                                                      properties={'sensor_type': 'sensor_type',
                                                                  'timestamp': 'timestamp',
                                                                  'sensor_ID': 'sensor_id',
                                                                  'data': 'data'}), name='sensor_geojson'),

    path('latest_sensor.geojson', LatestSensorGeoJSONLayerView.as_view(model=Sensor, geometry_field='coordinates',
                                                      properties={'sensor': 'sensor_type',
                                                                  'timestamp': 'timestamp',
                                                                  'sensor_id': 'sensor_id',
                                                                  'sensor_data': 'data'}), name='latest_sensor_geojson'),

    path('worldpoints', TemplateView.as_view(template_name='geo/points.html'), name='worldpoints_leaf'),
    path('worldborders', TemplateView.as_view(template_name='geo/borders.html'), name='worldborders_leaf'),
    path('linkstations', TemplateView.as_view(template_name='geo/link.html'), name='linkstations_leaf'),
    path('sensor', TemplateView.as_view(template_name='geo/sensor.html'), name='sensor_leaf'),
    path('latestsensor', TemplateView.as_view(template_name='geo/latestsensor.html'), name='latestsensor_leaf'),
]