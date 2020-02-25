from django.apps import apps
from django.test import TestCase
from django.urls import reverse

from djgeojson.views import GeoJSONLayerView
from djgeojson.serializers import Serializer

from .apps import GeoConfig
from .load import run_linkstation, run_worldborder
from .models import LINKStation, WorldBorder
from .views import GeoJSONSerializer

import json


class GeoConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(GeoConfig.name, 'geo')
        self.assertEqual(apps.get_app_config('geo').name, 'geo')


class GeoLoadTest(TestCase):

    def setUp(self):
        run_worldborder()
        run_linkstation()

    def test_geojson(self):
        # test linkstations geojson
        response = self.client.get(reverse('linkstations'))
        self.assertJSONEqual(json.dumps(response.json()), GeoJSONSerializer().serialize(LINKStation.objects.all(), crs=False, properties=('name',), use_natural_keys=True, with_modelname=False))

        ## test worldborder
        #response = self.client.get(reverse('worldborders'))
        #print(response.json())
        #self.assertJSONEqual(json.dumps(response.json()), Serializer().serialize(WorldBorder.objects.all(), crs=False, geometry_field='mpoly', properties=('name',), use_natural_keys=True, with_modelname=False))