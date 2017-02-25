from django.contrib import admin
from users.models import *
from django.contrib.auth import models

# Register your models here.
# admin.site.register(models.User)
admin.site.register(Guest)
admin.site.register(Waiter)
admin.site.register(Provider)
#