from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Trip, Vehicle, Passenger
# Create your views here.


""" 
    I have opted to use generic view to keep the code succint and readable, but
    it would have been just the same for me to reproduce the same result implementing
    the views myself.

    The little business logic necessary for this project is implemented through model methods. 
"""

class AddTripView(CreateView):
    model = Trip
    fields = '__all__' 
    template_name = 'create_trip.html'

class VehicleListView(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'vehicles.html'

class PassengerListView(ListView):
    model = Passenger
    context_object_name = 'passengers'
    template_name = 'passengers.html'