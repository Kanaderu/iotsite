from django.test import TestCase
from django.apps import apps

from .apps import DashboardConfig


class DashboardConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(DashboardConfig.name, 'dashboard')
        self.assertEqual(apps.get_app_config('dashboard').name, 'dashboard')