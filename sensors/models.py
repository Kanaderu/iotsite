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

'''
class LoRaGatewayData(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    app_id = models.CharField(max_length=128, blank=True, default='')
    dev_id = models.CharField(max_length=128, blank=True, default='')
    hardware_serial = models.CharField(max_length=128, blank=True, default='')
    port = models.IntegerField()
    counter = models.IntegerField()
    payload_raw = models.CharField(max_length=128, blank=True, default='')
    downlink_url = models.CharField(max_length=1024, blank=True, default='')

    class Meta:
        verbose_name = 'LoRa Gateway Data'
        verbose_name_plural = 'LoRa Gateway Data'
        ordering = ['metadata']


class LoRaGatewayPayloadFields(models.Model):
    gateway_data = models.OneToOneField('LoRaGatewayData', related_name='payload_fields', null=True, on_delete=models.CASCADE)

    b = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sm1 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sm2 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sm3 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sm4 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    t1 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    t2 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        verbose_name = 'LoRa Gateway Payload Field'
        verbose_name_plural = 'LoRa Gateway Payload Fields'


class LoRaGatewayMetadata(models.Model):
    gateway_data = models.OneToOneField('LoRaGatewayData', related_name='metadata', null=True, on_delete=models.CASCADE)

    time = models.DateTimeField(blank=True, null=True)
    frequency = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    modulation = models.CharField(max_length=128, blank=True, default='')
    data_rate = models.CharField(max_length=128, blank=True, default='')
    coding_rate = models.CharField(max_length=128, blank=True, default='')

    class Meta:
        verbose_name = 'LoRa Gateway Metadata'
        verbose_name_plural = 'LoRa Gateway Metadata'
        ordering = ['-time']


class LoRaGateway(models.Model):
    metadata = models.ForeignKey('LoRaGatewayMetadata', related_name='gateways', null=True, on_delete=models.CASCADE)

    gtw_id = models.CharField(max_length=128, blank=True, default='')
    gtw_trusted = models.BooleanField(default=False)
    timestamp = models.BigIntegerField(blank=True)
    time = models.CharField(max_length=128, blank=True, default='')
    channel = models.BigIntegerField(blank=True)
    rssi = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    snr = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    rf_chain = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    point = models.PointField(geography=True, default='POINT(0.0 0.0)')

    class Meta:
        verbose_name = 'LoRa Gateway'
        verbose_name_plural = 'LoRa Gateway'


class FeatherDataV2(models.Model):
    dev_id = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ['metadata']


class FeatherMetadataV2(models.Model):
    feather_data = models.OneToOneField('FeatherDataV2', related_name='metadata', null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=64, blank=True, default='')
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    point = models.PointField(geography=True, default='POINT(0.0 0.0)')
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-time']


class FeatherSensorDataV2(models.Model):
    feather_data = models.ForeignKey('FeatherDataV2', related_name='data', null=True, on_delete=models.CASCADE)
    sensor_id = models.PositiveIntegerField(blank=True)
    sensor_type = models.CharField(max_length=64, blank=True, default='')
    sensor_data = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    sensor_units = models.CharField(max_length=8, blank=True, default='')
'''


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
