from django.shortcuts import render
from users import serializers, models
from rest_framework import generics
from rest_framework import permissions
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailRetrieve(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer

class GuestList(generics.ListAPIView):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer

class GuestCreate(generics.CreateAPIView):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestRegisterSerializer



class UserLoginAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = serializers.UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

