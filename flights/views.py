# flights/views.py
from django.shortcuts import render, redirect
from .services import register_flight, search_flights, FlightServiceException,flight_repo
from .models import FlightRepository

def home_view(request):
    return redirect('register_flight')

def register_flight_view(request):
    if request.method == 'POST':
        airline_name = request.POST.get('airline_name')
        source_city = request.POST.get('source_city')
        destination_city = request.POST.get('destination_city')
        price = request.POST.get('price')
        has_meals = request.POST.get('has_meals') == 'on'

        try:
            register_flight(airline_name, source_city, destination_city, price, has_meals)
            return render(request, 'flights/register.html', {'message': 'Flight registered successfully!'})
        except FlightServiceException as e:
            return render(request, 'flights/register.html', {'error_message': str(e)})

    return render(request, 'flights/register.html')

def search_flights_view(request):
    if request.method == 'POST':
        source_city = request.POST.get('source_city')
        destination_city = request.POST.get('destination_city')
        meals = request.POST.get('meals') == 'on'

        try:
            min_hops_result, cheapest_flight_result = search_flights(source_city, destination_city, meals)
            return render(request, 'flights/search.html', {
                'min_hops_result': min_hops_result,
                'cheapest_flight_result': cheapest_flight_result,
            })
        except FlightServiceException as e:
            return render(request, 'flights/search.html', {'error_message': str(e), 'results': []})

    return render(request, 'flights/search.html')

flight_repo = FlightRepository()  
def list_flights_view(request):
    flights = flight_repo.get_all_flights()  # Get all registered flights
    return render(request, 'flights/list.html', {'flights': flights})
