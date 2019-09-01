from django.db import models
from django.urls import reverse
from thorn import ModelEvent, webhook_model

#@webhook_model(
#    sender_field='author.account.user',
#)
@webhook_model
class SensorData(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    package_id = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(blank=True, null=True)
    relay_id = models.CharField(max_length=100, blank=True, default='')
    sensor_id = models.CharField(max_length=100, blank=True, default='')
    sensor_type = models.CharField(max_length=100, blank=True, default='')
    units = models.DecimalField(max_digits=8, decimal_places=5)
    data = models.CharField(max_length=1, blank=True, default='')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    altitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    speed = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    climb = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        ordering = ['created']

    class webhooks:
        on_create = ModelEvent('sensor_data.created')
        on_change = ModelEvent('sensor_data.changed')
        on_delete = ModelEvent('sensor_data.removed')

        def payload(self, sensor_data):
            return {
                'package_id': sensor_data.package_id,
                'timestamp': sensor_data.timestamp,
                'units': sensor_data.units,
            }

    def get_absolute_url(self):
        return reverse('sensordata-detail', args=[str(self.id)])

