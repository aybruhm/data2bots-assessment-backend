# Django Imports
from django.urls import reverse

# Rest Framework Imports
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

# Third Party Imports
from rest_framework_simplejwt.tokens import RefreshToken

# Own Imports
from accounts.models import User
from products.models import Product, Order


# Initialize api client
client = APIClient()


class ProductsTestCase(APITestCase):
    """Test case to test products"""
    
    def setUp(self) -> None:
        self.user = User.objects.get_or_create(
            firstname="abram",
            lastname="israel",
            email="israel@test.com",
            username="israel",
            password="somereally_strongpassword_2002"
        )[0]
        self.product = Product.objects.create(
            title="Python Architecture",
            description="Know how the most popular web framework was built in a newspaper room",
            price=56,
            quantity=25
        )
        self.order = Order.objects.create(
            user=self.user,
            status="pending"
        )
        self.order.products.add(self.product)
    
    @property
    def bearer_token(self):
        """
        Get access token for user
        """
        user = User.objects.get(email="israel@test.com")
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    def test_get_all_user_orders(self):
        """
        Ensure we get all the orders of the logged-in user
        """
        
        url = reverse("products:user_orders")
        response = client.get(path=url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)