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
router.register('sensors/?', views.SensorViewSet)
router.register(r'LoRaGateway/?$(?i)', views.LoRaGatewaySensorViewSet, base_name='LoRaGateway')
router.register(r'Feather/?$(?i)', views.FeatherSensorViewSet, base_name='Feather')

urlpatterns = [
    re_path(r'^hooks/', include(('thorn.django.rest_framework.urls', 'thorn'), namespace='webhook')),
    re_path(r'^api/', include(router.urls)),

    re_path('openapi', get_schema_view(
        title='UD Sensors API',
        description='An API to interact with UD based Sensors',
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    ), name='openapi-schema'),

    re_path('docs/', TemplateView.as_view(
        template_name='sensors/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),

    re_path('live/', views.live_index, name='live'),
    re_path('live/<str:sensors>/', views.live_room, name='live-sensors'),
    re_path('darksky/', views.DarkSkyView.as_view())
]