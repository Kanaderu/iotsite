from django.test import TestCase
from django.apps import apps

from sensors.apps import SensorsConfig


class SensorsConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(SensorsConfig.name, 'sensors')
        self.assertEqual(apps.get_app_config('sensors').name, 'sensors')