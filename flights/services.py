# flights/services.py
from collections import defaultdict, deque
from heapq import heappop, heappush
from .models import Flight, FlightRepository

class FlightServiceException(Exception):
    """Custom exception for flight service errors."""
    pass

class FlightService:
    def __init__(self):
        self.flight_repo = FlightRepository()

    def register_flight(self, airline_name, source_city, destination_city, price, has_meals=False):
        # Register the flight with the repository
        flight = Flight(airline_name, source_city, destination_city, price, has_meals)
        self.flight_repo.add_flight(flight)

    def search_flights(self, source_city, destination_city, meals=False):
        # Fetch all flights with the specified criteria
        flights = self.flight_repo.get_all_flights()  # get all flights in repo
        flight_paths = defaultdict(list)
        
        for flight in flights:
            flight_paths[flight.source_city].append(flight)

        # Ensure paths can be found, else raise an exception
        min_hops_result = self.find_minimum_hops(flight_paths, source_city, destination_city)
        cheapest_flight_result = self.find_cheapest_flight(flight_paths, source_city, destination_city)

        if not min_hops_result[0] and not cheapest_flight_result[0]:
            raise FlightServiceException(f"No flights found from {source_city} to {destination_city}")

        return min_hops_result, cheapest_flight_result

    def find_minimum_hops(self, flight_paths, source_city, destination_city):
        queue = deque([(source_city, [])])  # (current city, path taken)
        visited = set()
        min_hops_path = []
        min_hops = float('inf')

        while queue:
            current_city, path = queue.popleft()

            if current_city == destination_city:
                if len(path) < min_hops:
                    min_hops = len(path)
                    min_hops_path = path
                continue

            if current_city in visited:
                continue
            visited.add(current_city)

            for flight in flight_paths[current_city]:
                if flight.destination_city not in visited:
                    queue.append((flight.destination_city, path + [flight]))

        total_cost = sum(flight.price for flight in min_hops_path) if min_hops_path else 0
        return min_hops_path, total_cost

    def find_cheapest_flight(self, flight_paths, source_city, destination_city):
        queue = [(0, source_city, [])]  # (current cost, current city, path taken)
        cheapest_path = []
        cheapest_cost = float('inf')

        while queue:
            total_cost, current_city, path = heappop(queue)

            if current_city == destination_city:
                if total_cost < cheapest_cost:
                    cheapest_cost = total_cost
                    cheapest_path = path
                continue

            for flight in flight_paths[current_city]:
                # Ensure we don’t revisit the same city in this path
                if flight.destination_city not in {f.destination_city for f in path}:
                    heappush(queue, (total_cost + flight.price, flight.destination_city, path + [flight]))

        return cheapest_path, cheapest_cost
