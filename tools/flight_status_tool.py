import json
from qwen_agent.tools.base import BaseTool, register_tool

@register_tool('flight_status_checker')
class FlightStatusChecker(BaseTool):
    """
    This class defines the tool for checking flight status.
    The `@register_tool` decorator makes it available to the Qwen Agent.
    """
    # A description for the LLM to understand what this tool does.
    description = 'Checks the real-time status of a flight using its flight number.'

    # Defines the parameters the LLM needs to provide to use this tool.
    parameters = [{
        'name': 'flight_number',
        'type': 'string',
        'description': 'The flight number, for example, "QA123" or "AirlineCode-FlightNumber".',
        'required': True
    }]

    def call(self, params: str, **kwargs) -> str:
        """
        The main logic of the tool. It gets called when the agent decides to use it.
        'params' is a string-formatted JSON with the arguments from the LLM.
        """
        try:
            # Safely parse the JSON string of parameters provided by the LLM
            p = json.loads(params)
            flight_number = p['flight_number'].upper() # Use .upper() for case-insensitive matching

            # --- Mock API Logic ---
            # In a real application, you would make an API call here.
            print(f'--- Tool "flight_status_checker" called with flight number: {flight_number} ---')
            
            mock_statuses = {
                "QA123": "On Time",
                "QA456": "Delayed by 2 hours due to weather",
                "QA789": "Cancelled"
            }
            
            status = mock_statuses.get(flight_number, "Flight number not found.")
            
            # The tool must return a string. We'll format it nicely.
            return json.dumps({"flight_number": flight_number, "status": status})

        except Exception as e:
            print(f"Error in flight_status_checker tool: {e}")
            return json.dumps({"error": "There was an error processing the flight number."})