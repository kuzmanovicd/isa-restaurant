from rest_framework import serializers

from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description_restaurant']

class RestaurantRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'description_restaurant']
    

    def create(self, data):
        r = Restaurant(name=data['name'])
        r.save()
        return r



#za  Menu     Dodao: Spiric
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant']


class MenuRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['restaurant']
    
    


#za MenuItem   Dodao: Spiric
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name_item', 'description_item', 'price_item', 'quantity_item', 'type_item', 'menu']


class MenuItemRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name_item', 'description_item', 'price_item', 'quantity_item', 'type_item', 'menu']
    
    

# za Regione
# Dodao: Spiric
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'is_frontSide', 'is_forSmoke', 'is_open', 'restaurant']


class RegionRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['is_frontSide', 'is_forSmoke', 'is_open', 'restaurant']