from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
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
    url('openapi', get_schema_view(
        title="UD Sensors API",
        description="An API to interact with UD based Sensors",
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    ), name='openapi-schema'),

    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    url('docs/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^ws/hooks/', include(('thorn.django.rest_framework.urls', 'thorn'))),
        url(r'^ws/api/', include(router.urls)),
    ]
