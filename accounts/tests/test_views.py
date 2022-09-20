# Native Imports
import json

# Django Imports
from django.urls import reverse

# Rest Framework Imports
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

# Third Party Imports
from rest_api_payload import success_response

# Own Imports
from accounts.models import User


# Initialize api client
client = APIClient()

class AccountsTestCase(APITestCase):
    
    """Test case to register user"""
    
    def setUp(self) -> None:
        self.valid_payload = {
            "firstname": "Israel",
            "lastname": "Abraham",
            "username": "abram",
            "password": "somereally_strongpassword_2002",
            "email": "abram@test.com",
        }
        self.invalid_payload = {
            "firstname": "Israel",
            "lastname": "",
            "password": "somereally_strongpassword_2002",
        }

    def test_valid_register_user(self):
        """
        Ensure we can create a new user object.
        """
        
        url = reverse("accounts:register_user")
        response = client.post(url, data=self.valid_payload, format="json")
        expected_data = success_response(status=True, message='User created successfully.', data=self.valid_payload)
        
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_invalid_register_user(self):
        """
        Ensure we can't create a new user object with invalid data.
        """
        
        url = reverse("accounts:register_user")
        response = client.post(url, data=self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        