from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import BaseUserManager
from users.models import User

# Serializers
class UserSerializer(ModelSerializer):
    # Serializer for user registration
    password = CharField(write_only=True, required=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash password
        return super().create(validated_data)

class LoginSerializer(ModelSerializer):
    # Serializer for user login
    class Meta:
        model = User
        fields = ['email', 'password']