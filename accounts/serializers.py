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
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id', 'uuid', 'firstname', 'lastname', 
            'username', 'email', 'is_active', 'is_staff', 
            'is_superuser', 
        )
        extra_kwargs = {
            'uuid': {'read_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
        }