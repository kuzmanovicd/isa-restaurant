from django.contrib import admin
from users.models import *
from django.contrib.auth import models

# Register your models here.
# admin.site.register(models.User)
admin.site.register(BasicUser)
admin.site.register(Guest)
admin.site.register(Waiter)
admin.site.register(Cook)
admin.site.register(Bartender)
admin.site.register(Provider)
admin.site.register(Friendship)