from rest_framework import serializers
from users.serializers import RestaurantManagerSerializer
from restaurant.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    owner = RestaurantManagerSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description_restaurant', 'address_restaurant', 'phone_restaurant', 'owner', 'restaurant_menu' ]
        read_only_fields = ('id', )

#za order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'date_created', 'menu_items']
        read_only_fields = ('id', 'date_created')

#za bill 
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'order_to_pay']
        read_only_fields = ('id',)



#za  Menu     Dodao: Spiric
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant']
        read_only_fields = ('id',)




#za MenuItem   Dodao: Spiric
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name_item', 'description_item', 'price_item', 'quantity_item', 'type_item', 'menu',]
        read_only_fields = ('id',)

class MenuSerializer2(serializers.ModelSerializer):     
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'menu_items']
        read_only_fields = ('id',)

# za Table
# Dodao: Spiric
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'is_free', 'region']
        read_only_fields = ('id',)

# za Regione
# Dodao: Spiric
class RegionSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ['id', 'is_frontSide', 'is_forSmoke', 'is_open', 'restaurant', 'tables', 'table_count', ]
        read_only_fields = ('id',)


###Dejan
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'coming', 'duration', 'guest', 'restaurant', 'reserved_tables','cancelled']

class ReservationSerializerDetail(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = ['id', 'coming', 'duration', 'guest', 'restaurant', 'reserved_tables','cancelled']

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['id', 'reservation', 'guest' ]
        read_only_fields = ('id',)

class InviteSerializerDetail(serializers.ModelSerializer):
    reservation = ReservationSerializerDetail(read_only=True)
    class Meta:
        model = Invite
        fields = ['id', 'reservation', 'guest', 'confirmed']
        read_only_fields = ('id','reservation', 'confirmed')


# smena serializers
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'name_shift', 'begin', 'end', 'restaurant',]
        read_only_fields = ('id',)



# porudzbina serializers
class ItemsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsRequest
        fields = ['id', 'items', 'price_accepted', 'restaurant']
        read_only_fields = ('id',)


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = ['id', 'menu_item', 'quantity',]
        read_only_fields = ('id',)


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'request', 'price', 'accepted']
        read_only_fields = ('id', 'accepted',)