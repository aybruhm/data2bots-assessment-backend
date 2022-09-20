# Django Imports
from django.urls import path

# Own Imports
from accounts.views import (
    RegisterUserAPIView
)


app_name = "accounts"


urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register_user")
]
