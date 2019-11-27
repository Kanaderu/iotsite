import json
from urllib.request import urlopen
from rest_framework import permissions
from rest_framework.views import APIView
from django.conf import settings
from django.http import JsonResponse, Http404
from django.utils.timezone import utc
import datetime
from .models import DarkSky


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
