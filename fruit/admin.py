from django.contrib import admin
from .models import Fruit,Places

# Register your models here.

class FruitAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Fruit, FruitAdmin)

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Places, PlacesAdmin)
