from django.db import models
from django.contrib.auth.models import User
from restaurant.models import *
import hashlib

# Create your models here

class Guest(User):
    """
    Model za gosta platforme.
    """
    city = models.CharField(max_length=50, blank=True, default='')
    is_activated = models.BooleanField(null=False, default=False)
    activation_code = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.first_name

    def gen_activation_code(self):
        """
        Jedinstveni aktivacioni kod za datog gosta.
        """
        hash_source = self.username + self.password + 'isa'
        self.activation_code = hashlib.md5(hash_source.encode('utf8')).hexdigest()

    def activate(self, code):
        if code == self.activation_code:
            self.is_activated = True
            self.save()
        
        return self.is_activated

    def save(self, *args, **kwargs):
        self.gen_activation_code()
        super(Guest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    

class Employee(User):
    """
    Zaposleni u restoranu.
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return ' '.join([self.first_name, self.username, self.restaurant.name])

class Waiter(Employee):
    """
    Model za konobara platforme u jednom restoranu.
    """
    region = models.IntegerField(null=False)
    class Meta:
        verbose_name = 'Waiter'
        verbose_name_plural = 'Waiters'



# Model: Provider (dobavljac)
# Polja: naziv, ostalo iz usera
# Sadrzi: --
# Dodao: Spiric
class Provider(User):
    naziv = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'


# Model: RestaurantManager (Menadzer restorana)
# Polja: 
# Sadrzi
# Dodao: Spiric
class RestaurantManager(User):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)