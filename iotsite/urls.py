"""iotsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from graphene_django.views import GraphQLView
from iotsite.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sensors.urls')),
    path('', include('external_api.urls')),
    path('', include('geo.urls')),
    path('', include('users.urls')),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', include('geo.urls')),
    path('vehicle/', include('vehicles.urls')),
    path('', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('explorer/', include('explorer.urls')),
    ]
