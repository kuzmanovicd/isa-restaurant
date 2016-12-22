from django.db import models
from django.contrib.auth.models import (BaseUserManager, User)

# Create your models here

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Korisnici moraju imati email adresu')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        # user.save(using)

class AbstractUser(models.Model):
    """
    Abstract user that every user will inherit
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=70, null=True)
    image = models.ImageField()
    is_verified = models.BooleanField(default=False)
    activation_code = models.TextField(max_length=30, null=True)

    def __str__(self):
        return str("nesto")


class Guest(AbstractUser):
    pass