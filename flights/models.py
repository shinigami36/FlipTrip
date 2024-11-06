class Flight:
    def __init__(self, airline_name, source_city, destination_city, price, has_meals=False):
        self.airline_name = airline_name
        self.source_city = source_city
        self.destination_city = destination_city
        self.price = price  
        self.has_meals = has_meals
        
    def __str__(self):
        return f"{self.source_city} to {self.destination_city} via {self.airline_name} for ${self.price} {'(meals available)' if self.has_meals else ''}"

    def number_of_hops(self):
        return 1  
    def total_cost(self):
        return self.price

class FlightRepository:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, source_city, destination_city=None, meals=False):
        # Search for flights that match source and, optionally, destination and meals preference
        return [
            flight for flight in self.flights
            if flight.source_city == source_city and 
               (destination_city is None or flight.destination_city == destination_city) and
               (flight.has_meals == meals or meals is None)
        ]


    def get_all_flights(self):
        return self.flights  # Return all registered flights