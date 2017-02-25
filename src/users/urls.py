from django.conf.urls import url, include
from users.views import *
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'guest_test', GuestViewSet)

urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'^all/?$', UserList.as_view(), name='user_list'),
    url(r'^(?P<pk>[0-9]+)/?$', UserDetailRetrieve.as_view(), name='rud_user'),
    url(r'^guests/all/?$', GuestList.as_view(), name='guest_list'),
    url(r'^guests/(?P<pk>[0-9]+)/?$', GuestDetail.as_view(), name='rud_guest'),
    url(r'^guests/create/?$', GuestCreate.as_view(), name='guest_create'),
    url(r'^activate/(?P<code>[a-z0-9]{32})/?$', ActivateGuestView.as_view(), name='guest_activate'),
    url(r'^csrf/?$', CSRFView.as_view(), name='csrf_token'),

    #url(r'^(?P<pk>[0-9]+)/?$', UserDetailRetrieve.as_view(), name='rud_user'),

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