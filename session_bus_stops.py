import requests

def getLatLongFromPostcode():
    r = requests.get('https://api.postcodes.io/postcodes/GU50BD')
    print(r.text)


getLatLongFromPostcode()