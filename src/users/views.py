from django.shortcuts import render
from users import serializers, models
from rest_framework import generics
from rest_framework import permissions
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.core import exceptions
from django.contrib.auth import hashers

from django.core.mail import EmailMessage

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = models.BasicUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailRetrieve(generics.RetrieveAPIView):
    queryset = models.BasicUser.objects.all()
    serializer_class = serializers.UserSerializer

### Guest begin
class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer

class GuestList(generics.ListAPIView):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer

class GuestCreate(generics.CreateAPIView):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.validated_data['password'] = hashers.make_password(serializer.validated_data['password'])
        serializer.save()
        location = '/api/users/activate/'
        g = models.Guest.objects.get(username=serializer.validated_data['username'])
        location += g.activation_code
        full_path = self.request.build_absolute_uri(location)

        msg = EmailMessage('ISA Restaurant - Activation', 
        'Please activate your account here: ' + full_path, 
        to=[serializer.validated_data['email']])

        msg.send()

### Guest End

class ActivateGuestView(APIView):
    def get(self, request, code):
        try:
            guest = models.Guest.objects.get(activation_code=code)
            if not guest == None:
                guest.activate(code)
            
            serializer = serializers.ActivationSerializer(guest)
            return Response(serializer.data)
        except exceptions.ObjectDoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class CSRFView(APIView):
    def get(self, request):
        return Response(status=HTTP_200_OK)

class GuestViewSet(viewsets.ModelViewSet):
    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer


#za Provider-a   Dodao:Spiric
class ProviderList(generics.ListAPIView):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class ProviderCreate(generics.CreateAPIView):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


# za RestaurantManager-a    Dodao: Spiric
class RestaurantManagerList(generics.ListAPIView):
    queryset = models.RestaurantManager.objects.all()
    serializer_class = serializers.RestaurantManagerSerializer


class RestaurantManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RestaurantManager.objects.all()
    serializer_class = serializers.RestaurantManagerSerializer


class RestaurantManagerCreate(generics.CreateAPIView):
    queryset = models.RestaurantManager.objects.all()
    serializer_class = serializers.RestaurantManagerSerializer
