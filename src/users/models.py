from django.db import models
from django.contrib.auth.models import User
import hashlib
import datetime
from django.utils import timezone

# Create your models here

USER_TYPE = (
    ('GU', 'GUEST'),
    ('WA', 'WAITER'),
    ('CO', 'COOK'),
    ('BA', 'BARTENDER'),
    ('PR', 'PROVIDER'),
    ('RM', 'RESTAURANT_MANAGER'),
    ('SM', 'SYSTEM_MANAGER'),
)

class BasicUser(User):
    user_type = models.CharField(max_length=2, choices=USER_TYPE, null=False)

    class Meta:
        verbose_name = 'Basic User'
        verbose_name_plural = 'Basic Users'

class Guest(BasicUser):
    """
    Model za gosta platforme.
    """
    city = models.CharField(max_length=50, blank=True, default='')
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
            self.is_active = True
            self.save()
        
        return self.is_active

    def save(self, *args, **kwargs):
        self.gen_activation_code()
        self.user_type = 'GU'
        super(Guest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user_a = models.ForeignKey(User, related_name="user_a")
    user_b = models.ForeignKey(User, related_name="user_b")
    accepted = models.NullBooleanField()

    def accept(self):
        self.accepted = True

    def reject(self):
        self.accepted = False

    class Meta:
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendships'


class Employee(BasicUser):
    """
    Zaposleni u restoranu.
    """
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=datetime.date.today)
    clothes_size = models.IntegerField(default=0)
    shoe_size = models.IntegerField(default=0)

    def __str__(self):
        return ' '.join([self.first_name])

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

#Waiter (konobar)
class Waiter(Employee):
    """
    Model za konobara u jednom restoranu.
    """
    region = models.IntegerField(null=False)
    

    def save(self, *args, **kwargs):
        self.user_type = 'WA'
        super(Waiter, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Waiter'
        verbose_name_plural = 'Waiters'

#Cook (kuvar)
class Cook(Employee):
    """
    Model za kuvara u jednom restoranu
    """
    def save(self, *args, **kwargs):
        self.user_type = 'CO'
        super(Cook, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Cook'
        verbose_name_plural = "Cooks"

#Bartender (sanker)
class Bartender(Employee):
    """
    Model za sankera u jednom restoranu
    """
    def save(self, *args, **kwargs):
        self.user_type = 'BA'
        super(Bartender, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Bartender'
        verbose_name_plural = 'Bartenders'


# Model: Provider (dobavljac)
# Polja: id, naziv, user name, type, email, passwor
# Sadrzi: --
# Dodao: Spiric
class Provider(BasicUser):
    naziv = models.CharField(max_length=50)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.user_type = 'PR'
        super(Provider, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'


# Model: RestaurantManager (Menadzer restorana)
# Polja: 
# Sadrzi
# Dodao: Spiric
class RestaurantManager(BasicUser):
    
    def save(self, *args, **kwargs):
        self.user_type = 'RM'
        super(RestaurantManager, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'RestaurantManager'
        verbose_name_plural = 'RestaurantManagers'

class SystemManager(BasicUser):

    def save(self, *args, **kwargs):
        self.user_type = 'SM'
        self.is_superuser = True
        super(SystemManager, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'System Manager'
        verbose_name_plural = 'System Managers'