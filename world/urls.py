from django.conf.urls import url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import WorldBorder

urlpatterns = [
    url(r'^worldpoints.geojson$', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='lat_lon', properties=('name',)), name='worldpoints'),
    url(r'^worldborders.geojson$', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='mpoly', properties=('name',)), name='worldborders'),

    url(r'^worldpoints$', TemplateView.as_view(template_name='world/points.html'), name='worldpoints_leaf'),
    url(r'^worldborders$', TemplateView.as_view(template_name='world/borders.html'), name='worldborders_leaf'),
]
