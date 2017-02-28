from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, FieldError
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

"""
class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(Guest, related_name='friendship_request_sent')
    to_user = models.ForeignKey(Guest, related_name='friendship_request_received')

    created = models.DateTimeField(default=timezone.now)
    rejected = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Friendship Request'
        verbose_name_plural = 'Friendship Requests'
        unique_together = ('from_user', 'to_user')

    #def __str__(self):
    #    return ' '.join([self.from_user, 'je poslao zahtev za prijateljstvo ka', self.to_user])

    def accept(self):
        relation1 = Friend.objects.create(from_user=self.from_user, to_user=self.to_user)
        relation2 = Friend.objects.create(from_user=self.to_user, to_user=self.from_user)

        self.delete()

        FriendshipRequest.objects.filter(from_user=self.to_user, to_user=self.from_user).delete()

        return True
    
    def reject(self):
        self.rejected = timezone.now()
        self.save()

"""

class FriendshipManager(models.Manager):

    def friends(self, user):
        qs = Friend.objects.select_related('from_user', 'to_user').filter(from_user=user).all()
        print(qs)
        return qs

    def friends2(self, user):
        qs = Friend.objects.select_related('from_user', 'to_user').filter(from_user=user).all()

    def create_friendship(self, user1, user2):
        relation1 = Friend.objects.create(from_user=user1, to_user=user2)
        relation2 = Friend.objects.create(from_user=user2, to_user=user1)

        return relation1

    def are_friends(self, user1, user2):
        q1 = Friend.objects.filter(to_user=user1, from_user=user2)
        q2 = Friend.objects.filter(to_user=user2, from_user=user1)

        if len(q1) or len(q2):
            return True
        else:
            return False
    """
    def requests(self, user):
        qs = FriendshipRequest.objects.select_related('from_user', 'to_user').filter(to_user=user).all()
        requests = list(qs)
        return requests

    def sent_requests(self, user):
        qs = FriendshipRequest.objects.select_related('from_user', 'to_user').filter(from_user=user).all()
        requests = list(qs)
        return requests
    
    def rejected_requests(self, user):
        qs = FriendshipRequest.objects.select_related('from_user', 'to_user').filter(to_user=user, rejected__isnull=False).all()
        rejected = list(qs)
        return rejected

    
    def add_friend(self, from_user, to_user):
        if from_user == to_user:
            raise ValidationError("Gosti ne mogu biti prijatelji sa sobom.")
        
        if self.are_friends(from_user, to_user):
            raise ValidationError("Vec su prijatelji.")

        request, created = FriendshipRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

        if created is False:
            raise ValidationError("Friendship vec postoji")

        return request
    """

class Friend(models.Model):
    to_user = models.ForeignKey(Guest, related_name='friends')
    from_user = models.ForeignKey(Guest, related_name='_unused_friend_relation')
    created = models.DateTimeField(default=timezone.now)

    objects = FriendshipManager()

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'
        unique_together = ('from_user', 'to_user')

    #def __str__(self):  
    #    return self.to_user, self.from_user

    def save(self, *args, **kwargs):
        if self.to_user == self.from_user:
            raise ValidationError("Gost ne moze da doda sebe za prijatelja")
        super(Friend, self).save(*args, **kwargs)

    

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