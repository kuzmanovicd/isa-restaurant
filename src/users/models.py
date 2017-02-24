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
    
    def __str__(self):
        return self.first_name

    def activation_code(self):
        """
        Jedinstveni aktivacioni kod za datog gosta.
        """
        hash_source = self.username + self.password + 'isa'
        return hashlib.md5(hash_source.encode('utf8')).hexdigest()

    def activate(self, code):
        if code == self.activation_code():
            is_activated = True
        
        return is_activated
    

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