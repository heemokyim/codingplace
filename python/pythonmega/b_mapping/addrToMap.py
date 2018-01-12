# Showing map from address
# step
# 0. get address
# 1. address -> coordinate
# 2. coordinate -> making map
# 3. show users map

# more features
# 1. embedding IP of requester inside map.html

from geopy.geocoders import Nominatim
import folium
import os
import datetime

geolocator=Nominatim()

def parametrize(address):
    tok=address.split()
    # Why format like this? refer to geopy_example.py
    return tok[3]+","+tok[1]+","+tok[0]+","+tok[4]+", KR"

def addr2coor(address):
    formatted=parametrize(address)
    return geolocator.geocode(formatted)

def coor2map(lat,lng):
    directory='maps/'
    f_name=datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')+'.html'

    map=folium.Map(location=[lat,lng],zoom_start=15)

    fg=folium.FeatureGroup(name='MyApp')
    fg.add_child(folium.Marker(location=[lat+0.0001,lng+0.0001],popup="Hi i am marker",icon=folium.Icon(color='green')))
    
    map.add_child(fg)

    if not os.path.exists(directory):
        os.makedirs(directory)

    # no ':' for Windows file path
    map.save(directory+f_name)
    print('Stored as '+directory+f_name)

def addr2map(address):
    # for test
    if address=='1':
        address="경기도 수원시 영통구 이의동 1257-1"

    loc=addr2coor(address)
    coor2map(loc.latitude, loc.longitude)

if __name__=="__main__":
    addr2map(input('Type your address : '))
