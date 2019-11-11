from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='home'),
    re_path(r'.*', TemplateView.as_view(template_name='dashboard/index.html'), name='misc-home')
]

if settings.DEBUG:
    urlpatterns += [
        path('ws/', TemplateView.as_view(template_name='dashboard/index.html')),
        re_path(r'ws/.*', TemplateView.as_view(template_name='dashboard/index.html'))
    ]
