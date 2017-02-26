from rest_framework import serializers
from users import models
from django.contrib.auth import get_user_model

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'user_type', 'is_active']
        read_only_fields = ('id', 'user_type', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class GuestSerializer(serializers.ModelSerializer):
    """
    user_type UVEK MORA DA BUDE READ_ONLY!!! 
    Za POST, PUT i DELETE metode ce se moci uneti nesto u ova polja ali to je samo greska na api/docs!
    NAPOMENA: Samo jedan serializer po modelu se sada koristi
    """
    class Meta:
        model = models.Guest
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'city', 'user_type', ]
        read_only_fields = ('id', 'user_type', 'is_active')

        # zbog nekog glupog razloga, write-only polja moraju ovako
        extra_kwargs = {
            'password': {'write_only': True}
        }


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friendship
        fields = ['id', 'user_a', 'user_b', 'accepted']
        read_only_fields = ('id', 'user_a', 'accepted')

class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = ['id', 'is_active', 'activation_code' ]

class CSRFSerializer(serializers.Serializer):
    status = serializers.CharField()

#za Waiter-a 
class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Waiter
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'restaurant', 'user_type', 'region', 'date_of_birth', 'clothes_size', 'shoe_size']
        read_only_fields = ('id', 'user_type')

        extra_kwargs = {
            'password' : {'write_only' : True}
        }
#za Cook-a
class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cook
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'restaurant', 'user_type', 'date_of_birth', 'clothes_size', 'shoe_size']
        read_only_fields = ('id', 'user_type')

        extra_kwargs = {
            'password' : {'write_only' : True}
        }
#za Bartender-a
class BartenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bartender
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'restaurant', 'user_type', 'date_of_birth', 'clothes_size', 'shoe_size']
        read_only_fields = ('id', 'user_type')

        extra_kwargs = {
            'password' : {'write_only' : True}
        }



#za Probider-a  Dodao: Spiric
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = ['id', 'username', 'email', 'password', 'naziv', 'user_type']
        read_only_fields = ('id', 'user_type')

        extra_kwargs = {
            'password' : {'write_only' : True}
        }



# za RestaurantManager-a     Dodao: Spiric
class RestaurantManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RestaurantManager
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'restaurant', 'user_type']
        read_only_fields = ('id', 'user_type')

        extra_kwargs = {
            'password' : {'write_only' : True}
        }

