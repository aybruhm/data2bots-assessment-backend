# Rest Framework Imports
from rest_framework import serializers

# Own Imports
from accounts.models import User


class RegisterUserSerializer(serializers.Serializer):
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    def save(self, **kwargs):
        print("Kwargs: ", kwargs)
        # create and save user to database
        return super().save(**kwargs)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id', 'uuid', 'firstname', 'lastname', 
            'username', 'email', 'is_active', 'is_staff', 
            'is_superuser', 
        )