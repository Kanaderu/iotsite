from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import path
from rest_framework import routers, permissions
from rest_framework.schemas import get_schema_view
from sensors import views

router = routers.DefaultRouter()
#router.get_api_root_view().cls.__name__ = "UD Root"
#router.get_api_root_view().cls.__doc__ = "Your Description"
router.register(r'sensors', views.SensorViewSet)
router.register(r'LoRaGateway', views.LoRaGatewaySensorViewSet, base_name='LoRaGateway')
router.register(r'Feather', views.FeatherSensorViewSet, base_name='Feather')

urlpatterns = [
    url(r'^hooks/', include(('thorn.django.rest_framework.urls', 'thorn'), namespace='webhook')),
    url(r'^api/', include(router.urls)),
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.
    path('[w][s]/openapi', get_schema_view(
        title="UD Sensors API",
        description="An API to interact with UD based Sensors",
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    ), name='openapi-schema'),

    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    url('docs/', TemplateView.as_view(
        template_name='sensors/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),

    path('live/', views.live_index, name='live'),
    path('live/<str:sensors>/', views.live_room, name='live-sensors'),
]

if settings.DEBUG:
    urlpatterns += [
        url('ws/docs/', TemplateView.as_view(
            template_name='sensors/redoc.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='ws-redoc'),
        url('ws/openapi', get_schema_view(
            title="UD Sensors API",
            description="An API to interact with UD based Sensors",
            permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
        ), name='ws-openapi-schema'),
        url(r'^ws/hooks/', include(('thorn.django.rest_framework.urls', 'thorn'))),
        url(r'^ws/api/', include(router.urls)),
        path('ws/live/', views.live_index, name='ws-live'),
        path('ws/live/<str:sensors>/', views.live_room, name='ws-live-sensors'),
    ]
