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
    serializer_class = serializers.RestaurantSerializer

#za order
class OrderList(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderCreate(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

#za bill
class BillList(generics.ListAPIView):
    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer

class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer

class BillCreate(generics.CreateAPIView):
    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer





#za Menu   Dodao: Spiric
class MenuList(generics.ListAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class MenuCreate(generics.CreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


#za MenuItem   Dodao:Spiric
class MenuItemList(generics.ListAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class MenuItemCreate(generics.CreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


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
    serializer_class = serializers.RegionSerializer



# za Table
# Dodao: Spiric
class TableList(generics.ListAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer


class TableCreate(generics.CreateAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer
