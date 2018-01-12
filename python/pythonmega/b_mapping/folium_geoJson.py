import folium
import os

map = folium.Map(location=[37.304240, 127.047337],zoom_start=6,tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="My Map")

import pandas as pds
data=pds.read_csv('files/Volcanoes_USA.txt')

def coloring(elev):
    color=None
    if elev<2000:
        color='green'
    elif 2000<=elev<3000:
        color='orange'
    elif 3000<=elev:
        color='red'
    return color

# adding circle markers
for lat,lng,name,stat,tpe,elev in zip(list(data['LAT']),list(data['LON']),list(data['NAME']),list(data['STATUS']),list(data['TYPE']),list(data['ELEV'])):
    popUp = folium.Popup(name+", "+stat+", "+tpe, parse_html=True)
    fg.add_child(folium.CircleMarker(location=[lat,lng],radius=10,fill=True,popup=popUp,color=coloring(elev)))

file_path_kor='../worldjson/countries/KOR.geo.json'
file_path_jpn='../worldjson/countries/JPN.geo.json'

# adding polygon layer from geoJson file
# where is geo json file? == https://github.com/johan/world.geo.json

fg.add_child(
folium.GeoJson(data=(open(file_path_kor,'r',encoding='utf-8-sig').read())))

fg.add_child(
folium.GeoJson(data=(open(file_path_jpn,'r',encoding='utf-8-sig').read())))

map.add_child(fg)

if not os.path.exists('maps'):
    os.makedirs('maps')
map.save("maps/folium_geoJson.html")
