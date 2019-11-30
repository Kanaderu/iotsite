from django.conf import settings
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'live/(?P<sensors>\w+)/$', consumers.SensorConsumer),
]

if settings.DEBUG:
    websocket_urlpatterns += [
        re_path(r'ws/live/(?P<sensors>\w+)/$', consumers.SensorConsumer),
    ]