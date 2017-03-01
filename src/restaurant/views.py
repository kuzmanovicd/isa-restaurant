from django.shortcuts import render
from restaurant import models
from restaurant import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta
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
            
            #print(request.data)
            serializer = serializers.ReservationSerializer(data=request.data)

            if serializer.is_valid():
                duration = timedelta(hours=request.data['duration'])
                coming = parse_datetime(request.data['coming'])
                coming_end = coming + duration

                qs = models.Reservation.objects.filter(reserved_tables__in=request.data['reserved_tables'] )
                qs2 = models.Table.objects.filter(reservations__in=qs).distinct()
                qs3 = models.Reservation.objects.filter(reserved_tables__in=qs2)

                is_overlapping = False

                for q in qs3:
                    table_start = q.coming
                    table_end = table_start + timedelta(hours=q.duration)

                    print(table_start, ' - ', table_end)

                    if coming_end > table_start and coming_end <= table_end:
                        print('first case')
                        is_overlapping = True
                    elif coming >= table_start and coming <= table_end:
                        print('second case')
                        is_overlapping = True
                    elif coming < table_end and coming_end >= table_end:
                        print('third_case')
                        is_overlapping = True

                    if is_overlapping:
                        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)
          
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=HTTP_401_UNAUTHORIZED)

class InviteCreate(APIView):
    def post(self, request):
        #guest = users.models.Guest.objects.get(pk=request.user.id)
        print(request.data['guests'])
        is_done = True
        for g_id in request.data['guests']:
            data = {}
            data['guest'] = g_id
            data['reservation'] = request.data['reservation']

            serializer = serializers.InviteSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        if is_done:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_404_NOT_FOUND)


class MyInvitesView(generics.ListAPIView):

    serializer_class = serializers.InviteSerializerDetail
    def get_queryset(self):
        guest = users.models.Guest.objects.get(pk=self.request.user.id)
        return models.Invite.objects.filter(guest=guest)

class ConfirmInviteView(APIView):
    def post(self, request, id):
        try:
            guest = users.models.Guest.objects.get(pk=self.request.user.id)
            invite = models.Invite.objects.get(pk=id)
            confirm = request.data['confirm']
            invite.confirm(confirm)
            invite.save()
            return Response(status=HTTP_200_OK)
        except Exception as e:
            #print(e)
            return Response(status=HTTP_400_BAD_REQUEST)



# za smenu
class ShiftList(generics.ListAPIView):
    #queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer

    def get_queryset(self):
        rm = users.models.RestaurantManager.objects.get(pk=self.request.user.id)
        return models.Shift.objects.filter(restaurant=rm.working_in.id)


class ShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer


class ShiftCreate2(generics.CreateAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer



class ShiftCreate(APIView):
    def post(self, request):
        rm = users.models.RestaurantManager.objects.get(pk=request.user.id)
        request.data['restaurant'] = rm.working_in.id
        
        print(request.data)
        serializer = serializers.ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



    

class MakeOrder(APIView):
    def post(self, request, id):
    
        guest = users.models.Guest.objects.get(pk=self.request.user.id)
        invite = models.Invite.objects.get(pk=id)
        print(request.data)
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            invite.order = serializer.instance
            invite.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        
        return Response(status=HTTP_404_NOT_FOUND)

