from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})

class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
