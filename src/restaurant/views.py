from django.shortcuts import render
from restaurant import models
from restaurant import serializers
from rest_framework import generics

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})

class RestaurantList(generics.ListAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

class RestaurantCreate(generics.CreateAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantRegisterSerializer


#za Menu   Dodao: Spiric
class MenuList(generics.ListAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class MenuCreate(generics.CreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuRegisterSerializer


#za MenuItem   Dodao:Spiric
class MenuItemList(generics.ListAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class MenuItemCreate(generics.CreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemRegisterSerializer


# za Regione 
# Dodao: Spiric
class RegionList(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class RegionCreate(generics.CreateAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionRegisterSerializer