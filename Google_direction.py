# geocode the latitude and longitude of the destination and origin
from geopy.geocoders import Nominatim
geolocator = Nominatim()
origin = geolocator.geocode("2641 John F. Kennedy Blvd, Jersey City")
destination = geolocator.geocode(address)
address_start = {"latitude":origin.latitude,"longitude":origin.longitude}
address_end = {"latitude":destination.latitude,"longitude":destination.longitude}
print(address_start,'\n',address_end)

#Google Map Direction from origin to destination. Ask a request to search in
#google map and output the steps that can lead to the restaurant from your own location.
#The further development of this part, these descriptions for direction will be converted
#to voice that can help driver when they are driving.

import json, urllib
from urllib.parse import urlencode
import urllib.request
import googlemaps

start = "2641 John F. Kennedy Blvd, Jersey City"
finish = address

url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
            ('origin', start),
            ('destination', finish)
 ))
ur = urllib.request.urlopen(url)
result = json.load(ur)

for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    if '<b>' in j:
        j = j.replace('<b>','')
    if '</b>' in j:
        j = j.replace('</b>','') 
    if '</div>' in j:
        j = j.replace('</div>','')
    if '/' in j:
        j = j.replace('/','')
    if '<div style="font-size:0.9em">' in j:
        j = j.replace('<div style="font-size:0.9em">',"\n")
    print(j)
