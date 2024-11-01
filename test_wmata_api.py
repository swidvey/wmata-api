import json
import unittest
from wmata_api import app

class WMATATest(unittest.TestCase):
    # ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/ESCALATOR').status_code
        # assert that the response code of 'incidents/ESCALATOR returns a 200 code
        self.assertEqual(escalator_response, 200)

        elevator_response = app.test_client().get('/incidents/ELEVATOR').status_code
        # assert that the response code of 'incidents/elevators returns a 200 code
        self.assertEqual(elevator_response, 200)

################################################################################

    # ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get('/incidents/ESCALATOR')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response assert that each of the required fields
        # are present in the response
        for s in range(len(json_response)):
            dic_keys_ls = list(json_response[s].keys())
            self.assertEqual(set(required_fields), set(dic_keys_ls))


################################################################################

    # ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/ESCALATOR')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        for s in range(len(json_response)):
            unit_type_value = json_response[s]["UnitType"]
            self.assertEqual(unit_type_value, "ESCALATOR")

################################################################################

    # ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/ELEVATOR')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for s in range(len(json_response)):
            unit_type_value = json_response[s]["UnitType"]
            self.assertEqual(unit_type_value, "ELEVATOR")

################################################################################

if __name__ == "__main__":
    unittest.main()