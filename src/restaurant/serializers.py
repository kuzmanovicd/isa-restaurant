from rest_framework import serializers
from users.serializers import RestaurantManagerSerializer
from restaurant.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    owner = RestaurantManagerSerializer()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description_restaurant', 'address_restaurant', 'phone_restaurant', 'owner',]
        read_only_fields = ('id', )

#za  Menu     Dodao: Spiric
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant']
        read_only_fields = ('id',)


#za MenuItem   Dodao: Spiric
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name_item', 'description_item', 'price_item', 'quantity_item', 'type_item', 'menu']
        read_only_fields = ('id',)


# za Regione
# Dodao: Spiric
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'is_frontSide', 'is_forSmoke', 'is_open', 'restaurant']
        read_only_fields = ('id',)


# za Table
# Dodao: Spiric
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'row', 'column', 'is_free', 'region']
        read_only_fields = ('id',)

