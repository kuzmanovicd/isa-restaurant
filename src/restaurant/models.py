from django.db import models

# Create your models here.
#Model restorana
#Ima: naziv, opis, menu, konfiguraciju sedenja
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description_restaurant = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Menu(models.Model):
     restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

# model stavki menu-a restorana  Dodao: Spiric
# Ima: naziv, opis, cijenu, kolicinu, tip, id
class MenuItem(models.Model):
    name_item = models.CharField(max_length=50)
    description_item = models.CharField(max_length=50)
    price_item = models.DecimalField(max_digits=9, decimal_places=2)
    quantity_item = models.IntegerField()
    type_item = models.BooleanField(default=True)
    #restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_item


