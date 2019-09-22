from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from external_api import views

urlpatterns = [
    path('darksky/', views.DarkSkyView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
