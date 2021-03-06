from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenObtainPairView, TokenRefreshSlidingView, TokenRefreshView, TokenVerifyView
from django.urls import include, path
from .views import CreateAccountView, LogoutView, GetSlidingTokenView


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('api/logout/', LogoutView.as_view(), name='user-logout'),
    path('api/refresh/', TokenRefreshView.as_view(), name='user-refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('api/register/', CreateAccountView.as_view(), name='user-register'),
    #path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
    #path('api/refresh-token/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/token/', GetSlidingTokenView.as_view(), name='api-token'),
    #path('', include('django.contrib.auth.urls')),
]