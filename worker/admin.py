from django.contrib import admin
from .models import Country,City,Worker

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name','category']