# Django Imports
from django.urls import path

# Own Imports
from accounts.views import (
    RegisterUserAPIView,
    UpdateUserInformationAPIView
)

# SimpleJWT Imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "accounts"


urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register_user"),
    path("update/", UpdateUserInformationAPIView.as_view(), name="get_update_user"),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
