from django.urls import path
from .views import register_flight_view, search_flights_view,list_flights_view

urlpatterns = [
    path('register/', register_flight_view, name='register_flight'),
    path('search/', search_flights_view, name='search_flights'),
    path('list/', list_flights_view, name='list_flights_view'),
]
