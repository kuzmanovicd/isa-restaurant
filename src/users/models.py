from django.db import models
from django.contrib.auth.models import User

# Create your models here
class BaseUser(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField(max_length=70, null=True)
    is_activated = models.BooleanField(default=False)
    activation_code = models.TextField(max_length=30, null=True)

    def __str__(self):
        return str(self.user.name)


class Gost(BaseUser):
    pass
