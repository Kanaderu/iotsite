from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += [
        path('ws/', TemplateView.as_view(template_name='dashboard/index.html')),
    ]
