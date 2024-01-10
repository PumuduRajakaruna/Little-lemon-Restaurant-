from django.db import models

# Create your models here.
class pizza(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)    
    pImage = models.URLField()
    
class Burger(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)    
    bImage = models.URLField()   