from django.conf.urls import url
from users.views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^all/?$', UserList.as_view(), name='user_list'),
    url(r'^(?P<pk>[0-9]+)/?$', UserDetailRetrieve.as_view(), name='rud_user'),
    url(r'^guests/all/?$', GuestList.as_view(), name='guest_list'),
    url(r'^guests/(?P<pk>[0-9]+)/?$', GuestDetail.as_view(), name='rud_guest'),
    url(r'^guests/create/?$', GuestCreate.as_view(), name='guest_create'),


    url(r'auth/', obtain_jwt_token),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
]