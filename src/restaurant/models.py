from django.db import models
from django.utils import timezone

# Create your models here.

# Model: Restaurant (Restoran)
# Polja: naziv, opis, menu, konfiguracija sedenja, adresa, broj telefona
# Sadrzi: 
# Dodao: Spiric
class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    description_restaurant = models.CharField(max_length=100)
    address_restaurant = models.CharField(max_length=50, default="adresa")
    phone_restaurant = models.CharField(max_length=50, default="broj_tel")

    def __str__(self):
        return self.name


# Model: Menu (Jelevnik)
# Polja: naziv, opis, cena, kolicina, tip
# Sadrzi: veza ka restoranu (jedan meni pripada jednom restoranu)
# Dodao: Spiric
class Menu(models.Model):
     restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)



#model: Order (narudzbina)
class Order(models.Model):   
    date_and_time = models.DateTimeField(default=timezone.now())
    
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
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    #jedna stavka iz menija moze se nalaziti na vise narudzbina (valjda ovako ide)
    #order = models.ForeignKey(Order, on_delete=None)

    def __str__(self):
        return self.name_item



# Model: Region   (regioni restorana)
# Polja: front/back, somoke/nosmoke, open/closed
# Sadrzi: veza ka restoranu  (jedan restoran ima vise regiona)
# Dodao: Spiric
class Region(models.Model):
    is_frontSide = models.BooleanField(default=True)
    is_forSmoke = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)




# Model: Table  (stolovi)
# Polja: red, kolona, slobodan/zauzet
# Sadrzi:  veza ka regionu (jedan region ima vise stolova)
# Dodao: Spiric
class Table(models.Model):
    row = models.IntegerField(null=False)
    column = models.IntegerField()
    is_free = models.BooleanField(default=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

