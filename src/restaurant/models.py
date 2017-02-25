from django.db import models

# Create your models here.
#Model restorana
#Ima: naziv, opis, menu, konfiguraciju sedenja
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description_restaurant = models.CharField(max_length=100)
    #menu = models.OneToOneField(Menu, on_delete=models.CASCADE)

    #ovo bi trebalo biti kao za tu konfiguraciju sedenja, ali nisam siguran
    rows = models.IntegerField()
    columns = models.IntegerField()
    tables = models.IntegerField()
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# model stavki menu-a restorana  Dodao: Spiric
# Ima: naziv, opis, cijenu, kolicinu, tip, id
class MenuItem(models.Model):
    name_item = models.CharField(max_length=50)
    description_item = models.CharField(max_length=50)
    price_item = models.DecimalField(max_digits=9, decimal_places=2)
    quantity_item = models.IntegerField()
    type_item = models.BooleanField(default=True)
    id_item = models.CharField(max_length=50)
    #restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_item


