from rest_framework import serializers ,exceptions  
from .models import *
from django.contrib.auth import authenticate

class User_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account is not activated')
        return data  # Return validated data with user information if needed
