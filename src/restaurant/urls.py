from django.conf.urls import url
from .views import *

urlpatterns = [
    #za Restoran  Dodao: Spiric
    url(r'^restaurant/all/?$', RestaurantList.as_view(), name='restaurant_list'),
    url(r'^restaurant/(?P<pk>[0-9]+)/?$', RestaurantDetail.as_view(), name='restaurant_rud'),
    url(r'^restaurant/create/?$', RestaurantCreate.as_view(), name='restaurant_create'),

    #za Menu      Dodao: Spiric
    url(r'^menu/all/?$', MenuList.as_view(), name='menu_list'),
    url(r'^menu/(?P<pk>[0-9]+)/?$', MenuDetail.as_view(), name='rud_menu'),
    url(r'^menu/create/?$', MenuCreate.as_view(), name='menu_icreate'),

    #za MenuItem  Dodao: Spiric
    url(r'^menu_item/all/?$', MenuItemList.as_view(), name='menu_item_list'),
    url(r'^menu_item/(?P<pk>[0-9]+)/?$', MenuItemDetail.as_view(), name='rud_menu_item'),
    url(r'^menu_item/create/?$', MenuItemCreate.as_view(), name='menu_item_create'),

    # za Regione
    # Dodao: Spiric
    url(r'^region/all/?$', RegionList.as_view(), name='region_list'),
    url(r'^region/(?P<pk>[0-9]+)/?$', RegionDetail.as_view(), name='rud_region'),
    url(r'^region/create/?$', RegionCreate.as_view(), name='region_create'),

]