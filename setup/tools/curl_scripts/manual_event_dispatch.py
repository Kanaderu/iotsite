#!/usr/bin/env python
from sensors.models import SensorData

sensor_data = SensorData.objects.all()[0]

on_create = SensorData.webhooks.events['on_create']
on_create.send(instance=sensor_data, data=sensor_data.webhooks.payload(sensor_data))
