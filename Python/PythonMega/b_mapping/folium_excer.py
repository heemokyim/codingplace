import folium
import os

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='Mapbox Bright')

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

# How did you find all below?
# 1. dir(folium)
# 2. find some proper
# 3. help(folium.proper)
for lat,lng,name,stat,tpe,elev in zip(list(data['LAT']),list(data['LON']),list(data['NAME']),list(data['STATUS']),list(data['TYPE']),list(data['ELEV'])):
    popUp = folium.Popup(name+", "+stat+", "+tpe, parse_html=True)
    fg.add_child(folium.CircleMarker(location=[lat,lng],radius=10,fill=True,popup=popUp,color=coloring(elev)))

map.add_child(fg)

if not os.path.exists('maps'):
    os.makedirs('maps')
map.save("maps/folium_excer.html")
