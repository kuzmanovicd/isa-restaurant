from django.db import models
from django.utils import timezone
import users

# Create your models here.

# Model: Restaurant (Restoran)
# Polja: naziv, opis, menu, konfiguracija sedenja, adresa, broj telefona
# Sadrzi: 
# Dodao: Spiric
class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    description_restaurant = models.CharField(max_length=100)
    address_restaurant = models.CharField(max_length=50)
    phone_restaurant = models.CharField(max_length=50)
    owner = models.OneToOneField(users.models.RestaurantManager, on_delete=models.CASCADE, related_name="working_in")

    def __str__(self):
        return self.name


# Model: Menu (Jelevnik)
# Polja: naziv, opis, cena, kolicina, tip
# Sadrzi: veza ka restoranu (jedan meni pripada jednom restoranu)
# Dodao: Spiric
class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name = "restaurant_menu")



#model: Order (narudzbina)
class Order(models.Model):   
    date_created = models.DateTimeField('date created', default=timezone.now)
    menu_items = models.ForeignKey('restaurant.MenuItem', on_delete=models.CASCADE, related_name="orders")
    
#model: Bill (racun)
class Bill(models.Model):
    order_to_pay = models.OneToOneField(Order, on_delete=models.CASCADE)




# Model: MenuItem (Stavka Menu-a)
# Polja: naziv, opis, cena, kolicina tip
# Sadrzi: veza ka menu (jedna menu ima vise tipova)
# Dodao: Spiric
class MenuItem(models.Model):
    name_item = models.CharField(max_length=50, null=False)
    description_item = models.CharField(max_length=50)
    price_item = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    quantity_item = models.IntegerField(null=False)
    type_item = models.BooleanField(default=True, null=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu_items")
    
    
    def __str__(self):
        return self.name_item


# Model: Region   (regioni restorana)
# Polja: front/back, somoke/nosmoke, open/closeds
# Sadrzi: veza ka restoranu  (jedan restoran ima vise regiona)
# Dodao: Spiric
class Region(models.Model):
    is_frontSide = models.BooleanField(default=True)
    is_forSmoke = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    table_count = models.IntegerField(default=1)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="regions")

    def __str__(self):
        return ' '.join([str(self.restaurant), 'broj stolova', str(self.table_count)])


# Model: Table  (stolovi)
# Polja: red, kolona, slobodan/zauzet
# Sadrzi:  veza ka regionu (jedan region ima vise stolova)
# Dodao: Spiric
class Table(models.Model):
    is_free = models.BooleanField(default=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='tables')

    def __str__(self):
        name = ''
        if self.is_free:
            name = 'Slobodan'
        else:
            name = 'Zauzet'
        return ' '.join([str(self.region), '-', name, str(self.pk)])


class Reservation(models.Model):
    coming = models.DateTimeField()
    duration = models.IntegerField()
    guest = models.ForeignKey('users.Guest', on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reserved_tables = models.ManyToManyField('restaurant.Table', related_name="reservations")
    #test = models.ManyToManyField('restaurant.Restaurant.regions.tables')

    def __str__(self):
        return ' '.join([str(self.coming), str(self.restaurant), '-', str(self.duration), 'sata'])


    



