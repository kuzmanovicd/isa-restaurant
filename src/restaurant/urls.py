from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^all$', RestaurantListAPIView.as_view(), name='restaurantlist'),
    url(r'$', RestaurantRUDAPIView.as_view(), name='restaurant_rud'),
    url(r'^food/all/?$', Food_MenuListAPIView.as_view(), name='food_menulist'),
    url(r'food$/?$', Food_MenuRUDAPIView.as_view(), name='food_menu_rud'),
]