from django.conf.urls import url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import WorldBorder, LINKStation

#from sensors.models import LoRaGateway, FeatherDataV2

urlpatterns = [
    url(r'^worldpoints.geojson$', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='lat_lon', properties=('name',)), name='worldpoints'),
    url(r'^worldborders.geojson$', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='mpoly', properties=('name',)), name='worldborders'),
    url(r'^linkstations.geojson$', GeoJSONLayerView.as_view(model=LINKStation, properties=('name',)), name='linkstations'),

    #url(r'^feather.geojson$', GeoJSONLayerView.as_view(model=FeatherDataV2.metadata, properties=('name',)), name='feather_geojson'),

    url(r'^worldpoints$', TemplateView.as_view(template_name='geo/points.html'), name='worldpoints_leaf'),
    url(r'^worldborders$', TemplateView.as_view(template_name='geo/borders.html'), name='worldborders_leaf'),
    url(r'^linkstations$', TemplateView.as_view(template_name='geo/link.html'), name='linkstations_leaf'),
]
