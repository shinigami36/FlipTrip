# main.py
from flights.services import FlightService, FlightServiceException

def driver():
    service = FlightService()

    # Register sample flights
    print("Registering sample flights...")
    try:
        service.register_flight("Jet Airways", "DEL", "BLR", 500, True)
        service.register_flight("Jet Airways", "BLR", "LON", 1000, True)
        service.register_flight("Delta", "DEL", "LON", 2000, True)
        service.register_flight("Indigo", "LON", "NYC", 2500, True)
        service.register_flight("Indigo", "DEL", "BLR", 600, True)
        service.register_flight("Indigo", "BLR", "PAR", 800, True)
        service.register_flight("Indigo", "PAR", "NYC", 3000, True)

        print("Sample flights registered successfully.\n")
    except FlightServiceException as e:
        print(f"Error registering flight: {e}")

    # Perform searches
    print("Searching for flights from DEL to NYC:")
    try:
        min_hops_result, cheapest_flight_result = service.search_flights("DEL", "NYC")
        print("Minimum Hops Result:")
        for flight in min_hops_result[0]:
            print(flight)
        print(f"Total Flights: {len(min_hops_result[0])}, Total Cost: ${min_hops_result[1]}\n")

        print("Cheapest Flight Result:")
        for flight in cheapest_flight_result[0]:
            print(flight)
        print(f"Total Flights: {len(cheapest_flight_result[0])}, Total Cost: ${cheapest_flight_result[1]}")
    except FlightServiceException as e:
        print(f"Error during flight search: {e}")

if __name__ == "__main__":
    driver()
