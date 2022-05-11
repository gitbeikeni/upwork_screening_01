from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Vehicle(models.Model):
    plate = models.CharField(max_length=10, primary_key=True)

    def total_km(self):
        return self.trips.aggregate(Sum('distance'))['distance__sum']

    def __str__(self):
        return self.plate

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='trips')
    distance = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    duration = models.DurationField() # DurationField in sqlite3 is represented with a bigint in microseconds
    passengers = models.ManyToManyField('trips.Passenger', related_name='trips') # optional through table to record departure times

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger')

    def get_vehicles(self):
        return { trip.vehicle: self.trips.filter(vehicle=trip.vehicle).aggregate(Sum('distance'))['distance__sum'] for trip in self.trips.all() }
        