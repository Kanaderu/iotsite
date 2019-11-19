from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenObtainPairView, TokenRefreshSlidingView, TokenRefreshView, TokenVerifyView
from django.urls import include, path
from .views import CreateAccountView, LogoutView
from django.conf import settings


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_login'),
    path('api/logout/', LogoutView.as_view(), name='token_logout'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', CreateAccountView.as_view())
    #path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
    #path('api/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    #path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('ws/api/login/', TokenObtainPairView.as_view(), name='db_token_login'),
        path('ws/api/logout/', LogoutView.as_view(), name='db_token_logout'),
        path('ws/api/refresh/', TokenRefreshView.as_view(), name='db_token_refresh'),
        path('ws/api/verify/', TokenVerifyView.as_view(), name='db_token_verify'),
        path('ws/api/register/', CreateAccountView.as_view())
        #path('ws/api/token/', TokenObtainSlidingView.as_view(), name='db_token_obtain_pair'),
        #path('ws/api/refresh/', TokenRefreshSlidingView.as_view(), name='db_token_refresh'),
    ]
