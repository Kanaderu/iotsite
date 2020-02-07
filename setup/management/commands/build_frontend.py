from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
import os


class Command(BaseCommand):
    """ Django command to build the frontend site """
    def handle(self, *args, **kwargs):
        os.system('cd dashboard && yarn build')
        self.stdout.write(self.style.SUCCESS('Built the frontend'))
