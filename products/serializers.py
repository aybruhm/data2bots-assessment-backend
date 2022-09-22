# Rest Framework Imports
from rest_framework import serializers

# Own Imports
from accounts.serializers import UserSerializer
from products.models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ["user", "products", "status"]