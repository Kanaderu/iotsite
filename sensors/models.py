from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from thorn import ModelEvent, webhook_model

#@webhook_model(
#    sender_field='author.account.user',
#)
@webhook_model
class SensorDataLtBigSense(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    timestamp = models.DateTimeField(blank=True, null=True)
    relay_id = models.CharField(max_length=100, blank=True, default='')
    sensor_id = models.CharField(max_length=100, blank=True, default='')
    sensor_type = models.CharField(max_length=100, blank=True, default='')
    units = models.DecimalField(max_digits=8, decimal_places=5)
    data = models.CharField(max_length=1, blank=True, default='')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    altitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    #point = models.PointField(geography=True, default='POINT(0.0 0.0)')
    speed = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    climb = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        verbose_name = 'Lt Sensor Data'
        verbose_name_plural = 'Lt Sensor Data'
        ordering = ['created']

    class webhooks:
        on_create = ModelEvent('sensor_data.created')
        on_change = ModelEvent('sensor_data.changed')
        on_delete = ModelEvent('sensor_data.removed')

        def payload(self, sensor_data):
            return {
                'id': sensor_data.id,
                'timestamp': sensor_data.timestamp,
                'units': sensor_data.units,
                'data': sensor_data.data,
                'longitude': sensor_data.longitude,
                'latitude': sensor_data.latitude,
                'altitude': sensor_data.altitude,
                'speed': sensor_data.speed,
                'climb': sensor_data.climb,
            }

    def get_absolute_url(self):
        return reverse('sensordata-detail', args=[str(self.id)])


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # add owner

    SENSOR_CHOICES = (
        ('LG', 'LoRa Gateway'),
        ('F', 'Feather'),
    )
    sensor = models.CharField(max_length=2, choices=SENSOR_CHOICES)
    sensor_id = models.CharField(max_length=64, blank=True)

    @property
    def coordinates(self):
        return self.metadata.coordinates

    @property
    def timestamp(self):
        return self.metadata.timestamp

    @property
    def sensor_data(self):
        return [model.to_dict for model in SensorData.objects.filter(sensor=self)]

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensor'
        ordering = ['-created']


class SensorMetadata(models.Model):
    sensor = models.OneToOneField('Sensor', related_name='metadata', null=True, on_delete=models.CASCADE)
    coordinates = models.PointField(geography=True, default='POINT(0.0 0.0)')
    timestamp = models.DateTimeField(blank=True, null=True)

    @property
    def sensor_type(self):
        return self.sensor.sensor

    @property
    def sensor_ID(self):
        return self.sensor.sensor_id

    @property
    def data(self):
        return self.sensor.sensor_data

    class Meta:
        verbose_name = 'Sensor Metadata'
        verbose_name_plural = 'Sensor Metadata'


class SensorData(models.Model):
    sensor = models.ForeignKey('Sensor', related_name='data', null=True, on_delete=models.CASCADE)
    data_id = models.CharField(max_length=64, blank=True)
    type = models.CharField(max_length=64, blank=True, default='')
    data = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    units = models.CharField(max_length=8, blank=True, default='')

    @property
    def to_dict(self):
        return { 'data_id': self.data_id,
                 'type': self.type,
                 'data': float(self.data),
                 'units': self.units}

    class Meta:
        verbose_name = 'Sensor Data'
        verbose_name_plural = 'Sensor Data'


class SensorRawData(models.Model):
    sensor = models.OneToOneField('Sensor', related_name='raw_data', null=True, on_delete=models.CASCADE)
    data = JSONField()

    class Meta:
        verbose_name = 'Raw Sensor Data'
        verbose_name_plural = 'Raw Sensor Data'
