# Django Imports
from django.urls import path

# Own Imports
from accounts.views import (
    RegisterUserAPIView,
    UpdateUserInformationAPIView
)


app_name = "accounts"


urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register_user"),
    path("update/<str:email>/", UpdateUserInformationAPIView.as_view(), name="get_update_user"),
]
