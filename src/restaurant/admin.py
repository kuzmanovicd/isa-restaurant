from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Region)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Invite)
admin.site.register(Shift)
admin.site.register(Order)

admin.site.register(ItemsRequest)
admin.site.register(ItemOrder)
admin.site.register(Offer)

