from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^restaurant/all/?$', RestaurantListAPIView.as_view(), name='restaurantlist'),
    url(r'^restaurant/?$', RestaurantRUDAPIView.as_view(), name='restaurant_rud'),
    #za MenuItem  Dodao: Spiric
    url(r'^menu_item/all/?$', MenuItemList.as_view(), name='menu_item_list'),
    url(r'^menu_item/(?P<pk>[0-9]+)/?$', MenuItemDetail.as_view(), name='rud_menu_item'),
    url(r'^menu_item/create/?$', MenuItemCreate.as_view(), name='menu_item_create'),
]