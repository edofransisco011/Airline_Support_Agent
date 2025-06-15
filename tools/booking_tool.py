import json
from qwen_agent.tools.base import BaseTool, register_tool

# Import the mock API client we created earlier
from utils.api_client import AirlineAPIClient

@register_tool('flight_search')
class SearchFlights(BaseTool):
    """
    This class defines the tool for searching for available flights.
    """
    # A description for the LLM to understand what this tool does.
    description = 'Searches for flights based on departure, destination, and date.'
    
    # Defines the parameters the LLM needs to provide to use this tool.
    parameters = [
        {
            'name': 'departure',
            'type': 'string',
            'description': 'The departure airport code, e.g., "JFK".',
            'required': True
        },
        {
            'name': 'destination',
            'type': 'string',
            'description': 'The destination airport code, e.g., "LAX".',
            'required': True
        },
        {
            'name': 'date',
            'type': 'string',
            'description': 'The desired date of travel, e.g., "2024-10-15".',
            'required': True
        }
    ]

    def call(self, params: str, **kwargs) -> str:
        """
        The main logic of the tool. It gets called when the agent decides to use it.
        """
        try:
            # Safely parse the JSON string of parameters provided by the LLM
            p = json.loads(params)
            departure = p.get('departure')
            destination = p.get('destination')
            date = p.get('date')

            # Instantiate our API client
            api_client = AirlineAPIClient()
            
            # Call the client's method to get flight data
            flight_results_json = api_client.search_flights(departure, destination, date)
            
            # Return the JSON results directly to the agent
            return flight_results_json

        except Exception as e:
            print(f"Error in flight_search tool: {e}")
            return json.dumps({"error": "There was an error searching for flights."})