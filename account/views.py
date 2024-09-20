from django.shortcuts import render
from pharmacies.models import *
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view ,APIView,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import status,filters
from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializer import *
from rest_framework.authtoken.serializers import AuthTokenSerializer


@api_view(['POST'])
def login_view(request):
    serializer = User_serializer(data=request.data)
    if serializer.is_valid():
       print(serializer.data)

       username = serializer.validated_data['username']
       password = serializer.validated_data['password']
       user = authenticate(username=data.get('username'), password=data.get('password'))
       print(user)
       if user is not None:
           token, created = Token.objects.get_or_create(user=user)
           return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
       else :
           print(serializer.data)

           return Response({'error': 'Invalid credentials' }, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sinup(request):
    serializer=Pharamcy_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(seralizer.data,status=status.HTTP_200_OK)
        
        