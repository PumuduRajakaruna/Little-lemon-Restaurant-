from django.contrib import admin
from .models import pizza 
from .models import Burger

# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'priceM', 'priceL']   

admin.site.register(pizza, PizzaAdmin)

class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'priceM', 'priceL']   

admin.site.register(Burger, BurgerAdmin)
