from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *
from django.contrib.auth import models

# Register your models here.
# admin.site.register(models.User)
admin.site.register(BasicUser, UserAdmin)
admin.site.register(Guest, UserAdmin)
admin.site.register(Waiter, UserAdmin)
admin.site.register(Cook, UserAdmin)
admin.site.register(Bartender, UserAdmin)
admin.site.register(Provider, UserAdmin)
admin.site.register(Friend)
admin.site.register(Employee, UserAdmin)
admin.site.register(RestaurantManager, UserAdmin)
