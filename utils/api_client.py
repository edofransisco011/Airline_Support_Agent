import json

class AirlineAPIClient:
    """
    A mock API client that simulates calls to a real airline's backend.
    It returns hardcoded data to ensure predictable behavior during development.
    """

    def search_flights(self, departure: str, destination: str, date: str) -> str:
        """
        Simulates searching for flights and returns the results as a JSON string.
        """
        print(f'--- Mock API called: Searching flights from {departure} to {destination} on {date} ---')

        # Mock data: In a real-world scenario, this would come from a live API.
        # We check for a specific route to show how different inputs can yield different results.
        if departure.lower() == 'jfk' and destination.lower() == 'lax':
            mock_flight_data = [
                {
                    "flight_number": "QA701",
                    "airline": "Qwen Airlines",
                    "departure_airport": "JFK",
                    "arrival_airport": "LAX",
                    "departure_time": "09:00",
                    "arrival_time": "12:00",
                    "price": 350.00,
                    "currency": "USD"
                },
                {
                    "flight_number": "QA703",
                    "airline": "Qwen Airlines",
                    "departure_airport": "JFK",
                    "arrival_airport": "LAX",
                    "departure_time": "17:00",
                    "arrival_time": "20:00",
                    "price": 420.50,
                    "currency": "USD"
                }
            ]
            return json.dumps(mock_flight_data)
        else:
            # Return an empty list if the route is not our primary test case.
            return json.dumps([])