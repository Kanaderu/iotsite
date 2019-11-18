from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView, TokenRefreshView, TokenVerifyView
from django.urls import include, path
from .views import CreateAccountView
from django.conf import settings


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', CreateAccountView.as_view())
    #path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('ws/api/token/', TokenObtainPairView.as_view(), name='db_token_obtain_pair'),
        path('ws/api/refresh/', TokenRefreshView.as_view(), name='db_token_refresh'),
        path('ws/api/verify/', TokenVerifyView.as_view(), name='db_token_verify'),
        path('ws/api/register/', CreateAccountView.as_view())
    ]
