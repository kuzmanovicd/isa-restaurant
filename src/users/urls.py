from django.conf.urls import url, include
from users.views import *
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'guest_test', GuestViewSet)

urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'^all/?$', UserList.as_view(), name='user-list'),
    url(r'^(?P<pk>[0-9]+)/?$', UserDetailRetrieve.as_view(), name='rud-user'),
    url(r'^guests/all/?$', GuestList.as_view(), name='guest-list'),
    url(r'^guests/(?P<pk>[0-9]+)/?$', GuestDetail.as_view(), name='rud-guest'),
    url(r'^guests/create/?$', GuestCreate.as_view(), name='guest-create'),
    url(r'^activate/(?P<code>[a-z0-9]{32})/?$', ActivateGuestView.as_view(), name='guest-activate'),
    url(r'^csrf/?$', CSRFView.as_view(), name='csrf-token'),

    url(r'^friends/?$', FriendshipCreate.as_view(), name='friendship-create'),
    url(r'^friends/delete/?$', FriendshipDelete.as_view(), name='friendship-delete'),
    url(r'^friends/my/?$', MyFriendsView.as_view(), name='my-friends'),

    #url(r'^(?P<pk>[0-9]+)/?$', UserDetailRetrieve.as_view(), name='rud_user'),

    #za waiter-a
    url(r'^waiter/all/?$', WaiterList.as_view(), name='waiter_list'),
    url(r'^waiter/(?P<pk>[0-9]+)/?$', WaiterDetail.as_view(), name='rud_waiter_detail'),
    url(r'^waiter/create/?$', WaiterCreate.as_view(), name='waiter_create'),

    #za cook-a
    url(r'^cook/all/?$', CookList.as_view(), name='cook_list'),
    url(r'^cook/(?P<pk>[0-9]+)/?$', CookDetail.as_view(), name='rud_cook_detail'),
    url(r'^cook/create/?$', CookCreate.as_view(), name='cook_create'),

    #za bartender-a
    url(r'^bartender/all/?$', BartenderList.as_view(), name='bartender_list'),
    url(r'^bartender/(?P<pk>[0-9]+)/?$', BartenderDetail.as_view(), name='rud_bartender_detail'),
    url(r'^bartender/create/?$', BartenderCreate.as_view(), name='bartender_detail'),


    # za Provider-a     Dodao: Spiric
    url(r'^provider/all/?$', ProviderList.as_view(), name='provider_list'),
    url(r'^provider/(?P<pk>[0-9]+)/?$', ProviderDetail.as_view(), name='rud_provider'),
    url(r'^provider/create/?$', ProviderCreate.as_view(), name='provider_create'),


    # za RestaurantManager-a     Dodao: Spiric
    url(r'^restaurant_manager/all/?$', RestaurantManagerList.as_view(), name='restaurant_manager_list'),
    url(r'^restaurant_manager/(?P<pk>[0-9]+)/?$', RestaurantManagerDetail.as_view(), name='rud_restaurant_manager'),
    url(r'^restaurant_manager/create/?$', RestaurantManagerCreate.as_view(), name='restaurant_manager_create'),


    url(r'^auth/?$', obtain_jwt_token),
    url(r'^verify/?$', verify_jwt_token),
]