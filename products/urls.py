# Django Imports
from django.urls import path

# Own Imports
from products.views import UserOrdersAPIView


app_name = "products"

urlpatterns = [
    path("orders/", UserOrdersAPIView.as_view(), name="user_orders"),
]