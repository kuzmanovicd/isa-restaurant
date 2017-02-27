from django.shortcuts import render
from users import serializers, models
from rest_framework import generics
from rest_framework import permissions
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
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
        g.is_active = False
        g.save()
        location += g.activation_code
        full_path = self.request.build_absolute_uri(location)

        msg = EmailMessage('ISA Restaurant - Activation', 
        'Please activate your account here: ' + full_path, 
        to=[serializer.validated_data['email']])

        msg.send()

### Guest End

class FrienshipCreate(APIView):
    def post(self, request, *args, **kwargs):
        guest = models.Guest.objects.filter(pk=request.user.id)[0]
        if guest.user_type == 'GU' and guest.id == request.data['user_b']:
            data = request.data
            data['user_a'] = guest.id
            serializer = serializers.FriendshipSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)



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


#za Waiter-a 
class WaiterList(generics.ListAPIView):
    queryset = models.Waiter.objects.all()
    serializer_class = serializers.WaiterSerializer

class WaiterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Waiter.objects.all()
    serializer_class = serializers.WaiterSerializer

class WaiterCreate(generics.CreateAPIView):
    queryset = models.Waiter.objects.all()
    serializer_class = serializers.WaiterSerializer

    def perform_create(self, serializer):
        serializer.validated_data['password'] = hashers.make_password(serializer.validated_data['password'])
        serializer.save()

#za Cook-a
class CookList(generics.ListAPIView):
    queryset = models.Cook.objects.all()
    serializer_class = serializers.WaiterSerializer

class CookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cook.objects.all()
    serializer_class = serializers.CookSerializer

class CookCreate(generics.CreateAPIView):
    queryset = models.Cook.objects.all()
    serializer_class = serializers.CookSerializer

    def perform_create(self, serializer):
        serializer.validated_data['password'] = hashers.make_password(serializer.validated_data['password'])
        serializer.save()

#za Bartender-a 
class BartenderList(generics.ListAPIView):
    queryset = models.Bartender.objects.all()
    serializer_class = serializers.BartenderSerializer

class BartenderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Bartender.objects.all()
    serializer_class = serializers.BartenderSerializer

class BartenderCreate(generics.CreateAPIView):
    queryset = models.Bartender.objects.all()
    serializer_class = serializers.BartenderSerializer

    def perform_create(self, serializer):
        serializer.validated_data['password'] = hashers.make_password(serializer.validated_data['password'])
        serializer.save()

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

    def perform_create(self, serializer):
        serializer.validated_data['password'] = hashers.make_password(serializer.validated_data['password'])
        serializer.save()
        


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

    def perform_create(self, serializer):
        serializer.validated_data['password'] = hashers.make_password(serializer.validated_data['password'])
        serializer.save()
