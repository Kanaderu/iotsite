from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(TemplateView.as_view(template_name='dashboard/index.html')), name='home'),
]

if settings.DEBUG:
    urlpatterns += [
        path('ws/', TemplateView.as_view(template_name='dashboard/index.html')),
        re_path(r'ws/.*', TemplateView.as_view(template_name='dashboard/index.html')),
        re_path(r'.*', csrf_exempt(TemplateView.as_view(template_name='dashboard/index.html')), name='misc-home'),
    ]
