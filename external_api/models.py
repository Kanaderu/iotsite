from django.db import models

# mysql
#from django_mysql.models import JSONField

# postgres
from django.contrib.postgres.fields import JSONField


class DarkSky(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    data = JSONField()
