from django.conf.urls import include, url
from rest_framework import routers
from sensors import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorDataViewSet)
router.register(r'LoRaGateway', views.LoRaGatewayDataView)

urlpatterns = [
    url(r'^hooks/', include(('thorn.django.rest_framework.urls', 'thorn'), namespace='webhook')),
    url(r'^api/', include(router.urls)),
]
