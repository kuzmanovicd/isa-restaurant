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
    url(r'^menu/restaurant/(?P<pk>[0-9]+)/?$', MenuForRestaurant.as_view(), name='r_menu'),
    url(r'^menu/create/?$', MenuCreate.as_view(), name='menu_icreate'),

    #za MenuItem  Dodao: Spiric
    url(r'^menu_item/all/?$', MenuItemList.as_view(), name='menu_item_list'),
    url(r'^menu_item/(?P<pk>[0-9]+)/?$', MenuItemDetail.as_view(), name='rud_menu_item'),
    url(r'^menu_item/create/?$', MenuItemCreate.as_view(), name='menu_item_create'),

    #api/users/employee/update/
    

    # za Regione
    # Dodao: Spiric
    url(r'^region/all/?$', RegionList.as_view(), name='region_list'),
    url(r'^region/(?P<restaurant>[0-9]+)/?$', RegionList.as_view(), name='region_list'),
    url(r'^region/(?P<pk>[0-9]+)/?$', RegionDetail.as_view(), name='rud_region'),
    url(r'^region/create/?$', RegionCreate.as_view(), name='region_create'),

    # za Table
    # Dodao: Spiric
    url(r'^table/all/?$', TableList.as_view(), name='table_list'),
    url(r'^table/(?P<pk>[0-9]+)/?$', TableDetail.as_view(), name='rud_table'),
    url(r'^table/create/?$', TableCreate.as_view(), name='table_create'),

    #za order 
    url(r'^order/all/?$', OrderList.as_view(), name='order_list'),
    url(r'^order/(?P<pk>[0-9]+)/?$', OrderDetail.as_view(), name='rud_order'),
    url(r'^order/create/?$', OrderCreate.as_view(), name='order_create'),

    #za bill 
    url(r'^bill/all/?$', BillList.as_view(), name='bill_list'),
    url(r'^bill/(?P<pk>[0-9]+)/?$', BillDetail.as_view(), name='rud_bill'),
    url(r'^bill/create/?$', BillCreate.as_view(), name='bill_create'),

    #reservacije
    url(r'^reservations/(?P<restaurant>[0-9]+)/?$', ReservationList.as_view(), name='reservation-for-restaurant'),
    url(r'^reservations/create/?$', ReservationCreate.as_view(), name='reservation-create'),
    url(r'^reservations/invite/create/?$', InviteCreate.as_view(), name='invite-create'),
    url(r'^reservations/invite/my/?$', MyInvitesView.as_view(), name='invites-my'),
    url(r'^reservations/invite/confirm/(?P<id>[0-9]+)/?$', ConfirmInviteView.as_view(), name='invites-confirm'),
    url(r'^reservations/my/?$', MyReservationsList.as_view(), name='reservations-my'),
    url(r'^reservations/cancel/(?P<id>[0-9]+)/?$', ReservationCancel.as_view(), name='reservations-my'),


    # za smenu
    url(r'^shift/all/?$', ShiftList.as_view(), name='shift_list'),
    url(r'^shift/(?P<restaurant>[0-9]+)/?$', ShiftDetail.as_view(), name='shift_rud'),
    url(r'^shift/create/?$', ShiftCreate.as_view(), name='shift_create'),

    #za item request ItemsRequestCreate
    url(r'^itemsrequest/create/?$', ItemsRequestCreate.as_view(), name='item-request-create'),
    #api/restaurant/reservation/make-order/
    url(r'^reservations/make-order/(?P<id>[0-9]+)/?$', MakeOrder.as_view(), name='make-order'),

    #ItemsRequestView
    url(r'^itemsrequest/all/?$', ItemsRequestList.as_view(), name='items_request_list'),
    url(r'^offer/create/?$', CreateOffer.as_view(), name='offer-create'),
    url(r'^offer/all/?$', OfferList.as_view(), name='offer-all'),
    

]