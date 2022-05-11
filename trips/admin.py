from django.contrib import admin

# Register your models here.
from .models import Vehicle, Trip, Passenger


class VehicleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vehicle._meta.fields]

admin.site.register(Vehicle, VehicleAdmin)

class TripAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Trip._meta.fields]

admin.site.register(Trip, TripAdmin)

class PassengerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Passenger._meta.fields]

admin.site.register(Passenger, PassengerAdmin)