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
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_activated', ]

class GuestRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = ['username', 'email', 'password', 'first_name', 'last_name', ]


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = ['id', 'is_activated', 'activation_code' ]


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    role = serializers.CharField(allow_blank=True)

    class Meta:
        model = User
        fields = [ 'username', 'password', 'token', 'role']
        extra_kwargs = {'password': 
            {'write_only': True}
        }

    def validate(self, data):
        username = data['username']
        password = data['password']
        user_a = User.objects.filter(username__iexact=username)
        user_b = User.objects.filter(email__iexact=username)
        user_qs = (user_a | user_b).distinct()

        if user_qs.exists() and user_qs.count() == 1:
            user_obj = user_qs.first()
            password_passes = user_obj.check_password(password)

            if type(user_obj) == models.Guest:
                if user_obj.is_activated == False:
                    serializers.ValidationError('Gost nije aktiviran')

            if password_passes:
                data['username'] = user_obj.username
#za Probider-a  Dodao: Spiric
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = ['id', 'username', 'email', 'password', 'naziv']


class ProviderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = ['username', 'email', 'password', 'naziv']

