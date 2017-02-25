from django.db import models

# Create your models here.

# Model: Restaurant (Restoran)
# Polja: naziv, opis, menu, konfiguracija sedenja
# Sadrzi: 
# Dodao: Spiric
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description_restaurant = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model: Menu (Jelevnik)
# Polja: naziv, opis, cena, kolicina, tip
# Sadrzi: veza ka restoranu (jedan meni pripada jednom restoranu)
# Dodao: Spiric
class Menu(models.Model):
     restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)


# Model: MenuItem (Stavka Menu-a)
# Polja: naziv, opis, cena, kolicina tip
# Sadrzi: veza ka menu (jedna menu ima vise tipova)
# Dodao: Spiric
class MenuItem(models.Model):
    name_item = models.CharField(max_length=50)
    description_item = models.CharField(max_length=50)
    price_item = models.DecimalField(max_digits=9, decimal_places=2)
    quantity_item = models.IntegerField()
    type_item = models.BooleanField(default=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_item


