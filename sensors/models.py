from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # TODO: record owner

    SENSOR_CHOICES = (
        ('LG', 'LoRa Gateway'),
        ('F', 'Feather'),
        #('M', 'Mobile App'),
    )
    sensor = models.CharField(max_length=2, choices=SENSOR_CHOICES)
    sensor_id = models.CharField(max_length=64, blank=True)
    coordinates = models.PointField(geography=True, default='POINT(0.0 0.0)')
    timestamp = models.DateTimeField()

    @property
    def sensor_data(self):
        return [model.to_dict for model in SensorData.objects.filter(sensor=self)]

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensor'
        ordering = ['-timestamp']


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


class DarkSky(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    data = JSONField()
