from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'live/(?P<sensors>\w+)/$', consumers.SensorConsumer.as_asgi()),
]
