import requests
import json

def getLatLongFromPostcode():
    r = requests.get('https://api.postcodes.io/postcodes/GU50BD')
    pretty_json = json.loads(r.text)
    return json.dumps(pretty_json, indent=2)

def getBusStops():
    r = requests.get('https://transportapi.com/v3/uk/bus/stop/490008660N/live.json?app_id=b4a74f33&app_key=7442a17ade5eaf611706d38c1a0b8c4a&group=route&nextbuses=yes')
    pretty_json = json.loads(r.text)
    return json.dumps(pretty_json.departures, indent=2)

getBusStops()