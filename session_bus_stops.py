import requests
import json

def getLatLongFromPostcode(postcode):
    r = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
    postcode = json.loads(r.text)
    return (postcode['result']['longitude'], postcode['result']['latitude'])


def getBusStop(route):
    r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{route}/live.json?app_id=b4a74f33&app_key=7442a17ade5eaf611706d38c1a0b8c4a&group=route&nextbuses=yes')
    bus_stop = json.loads(r.text)
    
    return bus_stop['departures'].values()

#getBusStops()
coord = (getLatLongFromPostcode('nw51tl'))
#print(getActoCodes(coord))