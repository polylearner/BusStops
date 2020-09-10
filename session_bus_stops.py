import requests
import json

def getLatLongFromPostcode():
    r = requests.get('https://api.postcodes.io/postcodes/GU50BD')
    pretty_json = json.loads(r.text)
    return json.dumps(pretty_json, indent=2)

def getBusStop(route):
    r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{route}/live.json?app_id=b4a74f33&app_key=7442a17ade5eaf611706d38c1a0b8c4a&group=route&nextbuses=yes')
    bus_stop = json.loads(r.text)
    
    return bus_stop['departures'].values()

#getBusStops()