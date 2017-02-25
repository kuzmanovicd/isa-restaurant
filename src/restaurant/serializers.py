from rest_framework import serializers

from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']

class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [ 'name' ]
    

    def create(self, data):
        r = Restaurant(name=data['name'])
        r.save()
        return r



#za MenuItem   Dodao: Spiric
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id_item', 'name_item', 'description_item', 'price_item', 'quantity_item', 'type_item']


class MenuItemRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id_item', 'name_item', 'description_item', 'price_item', 'quantity_item', 'type_item']
    
    