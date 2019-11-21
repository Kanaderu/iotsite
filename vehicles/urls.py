from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:vehicles>/', views.vehicles, name='vehicles'),
]

