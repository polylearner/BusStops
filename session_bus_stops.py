import requests
import json

def getLatLongFromPostcode():
    r = requests.get('https://api.postcodes.io/postcodes/GU50BD')
    pretty_json = json.loads(r.text)
    return json.dumps(pretty_json, indent=2)

def getBusStop1():
    r = requests.get('https://transportapi.com/v3/uk/bus/stop/490008660N/live.json?app_id=b4a74f33&app_key=7442a17ade5eaf611706d38c1a0b8c4a&group=route&nextbuses=yes')
    r2 = requests.get('https://transportapi.com/v3/uk/bus/stop/490008660S/live.json?app_id=b4a74f33&app_key=7442a17ade5eaf611706d38c1a0b8c4a&group=route&nextbuses=yes')
    bus_stop1 = json.loads(r.text)
    
    return bus_stop1['departures'].values()

def getBusStop2():
    r2 = requests.get('https://transportapi.com/v3/uk/bus/stop/490008660S/live.json?app_id=b4a74f33&app_key=7442a17ade5eaf611706d38c1a0b8c4a&group=route&nextbuses=yes')
    bus_stop2 = json.loads(r2.text)
    
    return bus_stop2['departures'].values()

#getBusStops()