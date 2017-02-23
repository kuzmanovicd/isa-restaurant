from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'all', UsersLISTAPIView.as_view(), name='userslist'),
    #url(r'$', RestaurantRUDAPIView.as_view(), name='restaurant_rud'),
]