from django.shortcuts import render
from users import serializers, models
from rest_framework import generics

# Create your views here.
class UsersLISTAPIView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()