from django.shortcuts import render
from restaurant import models
from restaurant import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from django.core.exceptions import ObjectDoesNotExist
import users

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

class MenuForRestaurant(generics.RetrieveAPIView):
    serializer_class = serializers.MenuSerializer2

    def get_queryset(self):
        r_id = self.kwargs['pk']
        return models.Menu.objects.filter(restaurant=r_id)


       
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
    #queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer

    def get_queryset(self):
        r_id = self.kwargs['restaurant']
        return models.Region.objects.filter(restaurant=r_id)


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class RegionCreate(APIView):
    def post(self, request):
        rm = users.models.RestaurantManager.objects.get(pk=request.user.id)
        request.data['restaurant'] = rm.working_in.id
        
        print(request.data)
        serializer = serializers.RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            region = serializer.instance
            for i in range(region.table_count):
                    models.Table.objects.create(region=region)
            #reg = models.Region.objects.get()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

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


class ReservationList(generics.ListAPIView):
    serializer_class = serializers.ReservationSerializer

    def get_queryset(self):
        r_id = self.kwargs['restaurant']
        return models.Reservation.objects.filter(restaurant=r_id)

class ReservationCreate(APIView):
    def post(self, request):
        try:
            guest = users.models.Guest.objects.get(pk=request.user.id)
            request.data['guest'] = guest.id
            
            serializer = serializers.ReservationSerializer(data=request.data)

            if serializer.is_valid():
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=HTTP_401_UNAUTHORIZED)