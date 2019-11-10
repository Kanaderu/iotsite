from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import include, path
from .views import CreateAccountView
from django.conf import settings


urlpatterns = [
    path('api/api-token-auth/', obtain_jwt_token),
    path('api/api-token-refresh/', refresh_jwt_token),
    path('api/api-token-verify/', verify_jwt_token),
    path('api/register/', CreateAccountView.as_view())
    #path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('ws/api/api-token-auth/', obtain_jwt_token),
        path('ws/api/api-token-refresh/', refresh_jwt_token),
        path('ws/api/api-token-verify/', verify_jwt_token),
        path('ws/api/register/', CreateAccountView.as_view())
    ]
