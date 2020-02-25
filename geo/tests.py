from django.test import TestCase
from django.apps import apps

from .apps import GeoConfig


class GeoConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(GeoConfig.name, 'geo')
        self.assertEqual(apps.get_app_config('geo').name, 'geo')