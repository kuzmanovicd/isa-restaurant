from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'all$', RestaurantListAPIView.as_view(), name='restaurantlist'),
    url(r'$', RestaurantRUDAPIView.as_view(), name='restaurant_rud'),
]