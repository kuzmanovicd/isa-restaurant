from django.shortcuts import render
from restaurant import models
from restaurant import serializers
from rest_framework import generics

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})

class RestaurantListAPIView(generics.ListAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

class RestaurantRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


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
