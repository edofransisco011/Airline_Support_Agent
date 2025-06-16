# tests/test_tools.py
import unittest
import json
from tools.flight_status_tool import FlightStatusChecker
from tools.flight_search_tool import SearchFlights

class TestTools(unittest.TestCase):

    def test_flight_status_checker_found(self):
        """Test the flight status checker for a known flight."""
        tool = FlightStatusChecker()
        params = json.dumps({"flight_number": "QA123"})
        result = tool.call(params)
        data = json.loads(result)
        self.assertEqual(data['status'], 'On Time')
        self.assertEqual(data['flight_number'], 'QA123')

    def test_flight_status_checker_not_found(self):
        """Test the flight status checker for an unknown flight."""
        tool = FlightStatusChecker()
        params = json.dumps({"flight_number": "XX999"})
        result = tool.call(params)
        data = json.loads(result)
        self.assertEqual(data['status'], 'Flight number not found.')

    def test_flight_search_found(self):
        """Test the flight search tool for a known route."""
        tool = SearchFlights()
        params = json.dumps({
            "departure": "JFK",
            "destination": "LAX",
            "date": "2024-10-15"
        })
        result = tool.call(params)
        data = json.loads(result)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['flight_number'], 'QA701')

    def test_flight_search_not_found(self):
        """Test the flight search tool for an unknown route."""
        tool = SearchFlights()
        params = json.dumps({
            "departure": "ABC",
            "destination": "XYZ",
            "date": "2024-10-15"
        })
        result = tool.call(params)
        data = json.loads(result)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()