import json
import requests
from flask import Flask

# Original API endpoint URL's and access keys
#WMATA_API_KEY = ""
#INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
#headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# Due to WMATA API Endpoint issue - Testing was completed with a mock WMATA API. 
# Removed URL
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"


################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])

def get_incidents(unit_type):
  # create an empty list called 'incidents'
  incidents_list = []

  # use 'requests' to do a GET request to the WMATA Incidents API
  # retrieve the JSON from the response
  response = requests.get(INCIDENTS_URL)
  response_json = response.json()['ElevatorIncidents']

  # iterate through the JSON response and retrieve all incidents matching 
  # 'unit_type' elevators or escalators
  for i in range(len(response_json)):
    # Grab dic object in list
    response_dic = response_json[i]

    # Subset to dic to the 4 fields and will be empty if not matching unit_type
    subset_dic = {k: response_dic[k] for k in response_dic 
                  if (k in ['StationCode', 'StationName', 'UnitName', 'UnitType']) 
                  and (response_dic['UnitType'] == f'{unit_type}')}

    if len(subset_dic) == 0:
        # len 0 implies wrong unit_type, goes to next sloop
        continue
    else:
        # Adds dic object to incidents_list
        incidents_list.append(subset_dic)

  # Return the list of incident dictionaries using json.dumps()
  return json.dumps(incidents_list) 

if __name__ == '__main__':
    app.run(debug=True)
