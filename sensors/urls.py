from django.conf.urls import include, url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from sensors import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorDataViewSet)
router.register(r'LoRaGateway', views.LoRaGatewayDataView)
router.register(r'Feather', views.FeatherDataView)

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
    ), name='openapi-schema'),

    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    url('docs/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]
