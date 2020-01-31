from django.conf import settings
from django.views.generic import TemplateView
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from rest_framework.schemas import get_schema_view
from sensors import views


class Router(routers.DefaultRouter):

    def __init__(self):
        super(routers.DefaultRouter, self).__init__()
        self.trailing_slash = '/?'


router = Router()
#router.get_api_root_view().cls.__name__ = "UD Root"
#router.get_api_root_view().cls.__doc__ = "Your Description"
router.register(r'(?i)sensors', views.SensorViewSet)
router.register(r'(?i)LoRaGateway', views.LoRaGatewaySensorViewSet, base_name='LoRaGateway')
router.register(r'(?i)Feather', views.FeatherSensorViewSet, base_name='Feather')

urlpatterns = [
    re_path(r'^hooks/', include(('thorn.django.rest_framework.urls', 'thorn'), namespace='webhook')),
    re_path(r'^api/', include(router.urls)),
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.
    re_path('openapi', get_schema_view(
        title="UD Sensors API",
        description="An API to interact with UD based Sensors",
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    ), name='openapi-schema'),

    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    re_path('docs/', TemplateView.as_view(
        template_name='sensors/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),

    re_path('live/', views.live_index, name='live'),
    re_path('live/<str:sensors>/', views.live_room, name='live-sensors'),
    re_path('darksky/', views.DarkSkyView.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        re_path('ws/docs/', TemplateView.as_view(
            template_name='sensors/redoc.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='ws-redoc'),
        re_path('ws/openapi', get_schema_view(
            title="UD Sensors API",
            description="An API to interact with UD based Sensors",
            permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
        ), name='ws-openapi-schema'),
        re_path(r'^ws/hooks/', include(('thorn.django.rest_framework.urls', 'thorn'))),
        re_path(r'^ws/api/', include(router.urls)),
        re_path('ws/live/', views.live_index, name='ws-live'),
        re_path('ws/live/<str:sensors>/', views.live_room, name='ws-live-sensors'),
    ]
