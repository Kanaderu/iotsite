from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from sensors import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorDataViewSet)

urlpatterns = [
    url(r'^hooks/', include(('thorn.django.rest_framework.urls', 'thorn'), namespace='webhook')),
    url(r'^api/', include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
