from rest_framework import serializers
from users import models
from django.contrib.auth import get_user_model

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', ]

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_activated', 'city', ]

class GuestRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'city',]
    
    """
    def create(self, validated_data):
        guest = models.Guest.objects.create_user(**validated_data)
        return guest
    """

class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = ['id', 'is_activated', 'activation_code' ]

class CSRFSerializer(serializers.Serializer):
    status = serializers.CharField()
    

#za Probider-a  Dodao: Spiric
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = ['id', 'username', 'email', 'password', 'naziv']


class ProviderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = ['username', 'email', 'password', 'naziv']



# za RestaurantManager-a     Dodao: Spiric
class RestaurantManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RestaurantManager
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'restaurant']


class RestaurantManagerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RestaurantManager
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'restaurant']

