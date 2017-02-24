from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# model jelovnika restorana
class Food_Menu(models.Model):
    food_name = models.CharField(max_length=50)
    #food_description = models.CharField(max_length=50)
    #food_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.food_name


#model karte pica restorana
class Drink_Map(models.Model):
    drink_name = models.CharField(max_length=50)
    drink_description = models.CharField(max_length=50)
    drink_price = models.DecimalField(max_digits=5, decimal_places=2)

   