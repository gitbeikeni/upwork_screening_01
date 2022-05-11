from django.urls import path
from . import views

urlpatterns = [
    path('add_trip/', views.AddTripView.as_view(), name='create_trip'),
    path('vehicles/', views.VehicleListView.as_view(), name='list_vehicles'),
    path('passengers/', views.PassengerListView.as_view(), name='list_passengers'),
]
