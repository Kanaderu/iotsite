from sensors.serializers import *
from rest_framework import viewsets, mixins, permissions
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# DarkSky
from urllib.request import urlopen
from rest_framework.views import APIView
from django.conf import settings
from django.http import JsonResponse, Http404
from django.utils.timezone import utc
import datetime
from .models import DarkSky

from djgeojson.views import GeoJSONLayerView


# modify queryset for the most recent data across all sensors
class LatestSensorGeoJSONLayerView(GeoJSONLayerView):
    def get_queryset(self):
        items = set()
        for sensor_type in Sensor.SENSOR_CHOICES:
            latest_item = Sensor.objects.filter(sensor=sensor_type[0]).order_by('-created').first()
            if latest_item is not None:
                items.add(latest_item.pk)

        context = Sensor.objects.filter(pk__in=items)
        return context


class SensorViewSet(viewsets.ModelViewSet):
    """
    The sensor list contains data received from  all the sensor data. Filters can be applied to search through the data.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = ['sensor', 'sensor_id']
    search_fields = ['sensor', 'sensor_id', 'data']
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    #filter_backends = (NameFilterBackend,)


class LoRaGatewaySensorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoRaGatewaySensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class FeatherSensorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = FeatherSensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


def live_index(request):
    return render(request, 'sensors/index.html', {})


def live_room(request, sensors):
    return render(request, 'sensors/room.html', {
        'sensors_json': mark_safe(json.dumps(sensors))
    })


class DarkSkyView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def __init__(self):
        key = settings.DARKSKY_KEY
        latitude = settings.DARKSKY_LAT
        longitude = settings.DARKSKY_LON
        #time = '' # TODO

        self.enabled = key is not None
        self.update_th = settings.DARKSKY_THRESH

        self.darksky_forcast_url = "https://api.darksky.net/forecast/{}/{},{}".format(key, latitude, longitude)
        #self.darksky_time_machine_url = "https://api.darksky.net/forecast/{}/{},{},{}".format(key, latitude, longitude, time)
        super(DarkSkyView, self)

    def get(self, request):
        if not self.enabled:
            raise Http404('DarkSky is not configured.')
        fetch_update = False
        response = None

        # get list of past queries, most recent first
        ds_queryset = DarkSky.objects.order_by('-created')

        # if empty
        if not ds_queryset:
            fetch_update = True
        else:
            last_query = ds_queryset[0]                             # last time updated
            now = datetime.datetime.utcnow().replace(tzinfo=utc)    # current time
            timedelta = now - last_query.created                    # time difference

            if timedelta.total_seconds() > self.update_th:
                # trigger update
                fetch_update = True
            else:
                # send latest saved query
                response = last_query.data

        if fetch_update:
            # fetch and save response into database
            output = urlopen(self.darksky_forcast_url).read()
            data = json.loads(output)
            DarkSky.objects.create(data=data)
        elif response is not None:
            data = response

        return JsonResponse(data)
