# Native Imports
import json

# Django Imports
from django.urls import reverse

# Rest Framework Imports
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

# Third Party Imports
from rest_api_payload import success_response
from rest_framework_simplejwt.tokens import RefreshToken

# Own Imports
from accounts.models import User
from accounts.serializers import UserSerializer


# Initialize api client
client = APIClient()

class AccountsTestCase(APITestCase):
    
    """Test case to register user"""
    
    def setUp(self) -> None:
        self.valid_register_payload = {
            "firstname": "Israel",
            "lastname": "Abraham",
            "username": "abram",
            "password": "somereally_strongpassword_2002",
            "email": "abram@test.com",
        }
        self.invalid_register_payload = {
            "firstname": "Israel",
            "lastname": "",
            "password": "somereally_strongpassword_2002",
        }
        self.login_payload = {
            "email": "abram@test.com",
            "password": "somereally_strongpassword_2002",
        }
        self.valid_update_user_payload = {
            "firstname": "Abraham",
            "lastname": "Israel",
            "username": "abram",
            "email": "abram@test.com",
        }
        self.invalid_update_user_payload = {
            "firstname": 3434,
            "lastname": "",
            "username": ""
        }
        self.user = User.objects.create(
            firstname="abram",
            lastname="israel",
            email="israel@test.com",
            username="israel",
            password="somereally_strongpassword_2002"
        )
        
    @property
    def bearer_token(self):
        """
        Get access token for user
        """
        user = User.objects.get(email="israel@test.com")
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}

    def test_valid_register_user(self):
        """
        Ensure we can create a new user object.
        """
        
        url = reverse("accounts:register_user")
        response = client.post(url, data=self.valid_register_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_invalid_register_user(self):
        """
        Ensure we can't create a new user object with invalid data.
        """
        
        url = reverse("accounts:register_user")
        response = client.post(url, data=self.invalid_register_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_get_valid_user(self):
        """
        Ensure we can get a single user
        """
        
        url = reverse("accounts:get_update_user")
        response = client.get(path=url, **self.bearer_token)     
        serializer = UserSerializer(self.user)
        serializer_data = success_response(status=True, message="User retrieved successfully.", data=serializer.data)

        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_valid_user(self):
        """
        Ensure we can update a user information
        """
        
        url = reverse("accounts:get_update_user")
        response = client.put(path=url, data=self.valid_update_user_payload, **self.bearer_token)     
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
    def test_update_invalid_user(self):
        """
        Ensure we can not update a user information with invalid data
        """
        url = reverse("accounts:get_update_user")
        response = client.put(path=url, data=self.invalid_update_user_payload, **self.bearer_token)     
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        