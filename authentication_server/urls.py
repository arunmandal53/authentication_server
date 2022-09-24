
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from user.views import (
    LoginAPIView,
    LogoutAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/login', LoginAPIView.as_view(), name="login"),
    path('api/v1/user/logout', LogoutAPIView.as_view(), name="logout"),

    path('api/v1/user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/user/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
