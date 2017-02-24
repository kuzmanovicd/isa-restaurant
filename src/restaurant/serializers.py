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



#za Food_Menu
class Food_MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Menu
        fields = ['id', 'food_name', ]


class Food_MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Menu
        fields = ['food_name']

        def create(self, data):
            f = Food_Menu(name=data['food_name'])
            
            return f
