from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(TemplateView.as_view(template_name='dashboard/index.html')), name='home'),
    re_path(r'.*', csrf_exempt(TemplateView.as_view(template_name='dashboard/index.html')), name='misc-home'),
]