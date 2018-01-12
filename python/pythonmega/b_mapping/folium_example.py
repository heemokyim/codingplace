# folium
# == make map html file from location arguments(longitude,latitude)

import folium
import os

        # -90<= latitude <= 90, -180<= longitude <=180
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='Mapbox Bright')
# help(folium.Map) == various tiles
# http://folium.readthedocs.io/en/latest/quickstart.html

# ---------------------------------------------------------

# 6. control panel
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

# group for volcanos
fgv = folium.FeatureGroup(name="Volcanoes")
for lat,lng,name,stat,tpe,elev in zip(list(data['LAT']),list(data['LON']),list(data['NAME']),list(data['STATUS']),list(data['TYPE']),list(data['ELEV'])):
    popUp = folium.Popup(name+", "+stat+", "+tpe, parse_html=True)

    iCon=folium.Icon(color=coloring(elev))
    fgv.add_child(folium.Marker(location=[lat,lng], popup=popUp, icon=iCon))

# group for populations
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(
folium.GeoJson(data=(open('files/world.json','r',encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}
))

# adding multiple base map
folium.TileLayer('OpenStreetMap').add_to(map)
folium.TileLayer('Mapbox Control Room').add_to(map)
# wait ! what about Mapboxbright?
# it is also reflected into control panel
# line 7

map.add_child(fgv)
map.add_child(fgp)
# adding panel after features
map.add_child(folium.LayerControl())

# 5. polygon layer using geoJson
# fg = folium.FeatureGroup(name="My Map")
#
# import pandas as pds
# data=pds.read_csv('files/Volcanoes_USA.txt')
#
# def coloring(elev):
#     color=None
#     if elev<2000:
#         color='green'
#     elif 2000<=elev<3000:
#         color='orange'
#     elif 3000<=elev:
#         color='red'
#     return color
#
# for lat,lng,name,stat,tpe,elev in zip(list(data['LAT']),list(data['LON']),list(data['NAME']),list(data['STATUS']),list(data['TYPE']),list(data['ELEV'])):
#     popUp = folium.Popup(name+", "+stat+", "+tpe, parse_html=True)
#
#     iCon=folium.Icon(color=coloring(elev))
#     fg.add_child(folium.Marker(location=[lat,lng], popup=popUp, icon=iCon))
#                                                 # safe to pass Popup-Object
#
# # To add polygon layer using geoJson file -> folium.GeoJson
# fg.add_child(
# folium.GeoJson(data=(open('files/world.json','r',encoding='utf-8-sig').read()),
# style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000
# else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}
# ))
#
# map.add_child(fg)

# 4. adding multiple features from file
# fg = folium.FeatureGroup(name="My Map")
#
# import pandas as pds
# data=pds.read_csv('files/Volcanoes_USA.txt')
#
# def coloring(elev):
#     color=None
#     if elev<2000:
#         color='green'
#     elif 2000<=elev<3000:
#         color='orange'
#     elif 3000<=elev:
#         color='red'
#     return color
#
# for lat,lng,name,stat,tpe,elev in zip(list(data['LAT']),list(data['LON']),list(data['NAME']),list(data['STATUS']),list(data['TYPE']),list(data['ELEV'])):
#     popUp = folium.Popup(name+", "+stat+", "+tpe, parse_html=True)
#
#     iCon=folium.Icon(color=coloring(elev))
#     fg.add_child(folium.Marker(location=[lat,lng], popup=popUp, icon=iCon))
#                                                 # safe to pass Popup-Object
# map.add_child(fg)

# 3. adding multiple features
# fg = folium.FeatureGroup(name="My Map")
#
# for each in [[37.55,128],[36.88,126.88]]:
#     fg.add_child( folium.Marker( location=each, popup=str(each), icon=folium.Icon(color='green') ))
#
# map.add_child(fg)

# 2. using group of features
# fg = folium.FeatureGroup(name='My map')
# fg.add_child(folium.Marker(location=[37.27,127.03],popup="Hi i am marker",icon=folium.Icon(color='green')))
# map.add_child(fg)

# 1. adding feature
# map.add_child(folium.Marker(location=[37.27,127.03],popup="Hi i am marker",icon=folium.Icon(color='green')))

# ---------------------------------------------------------
if not os.path.exists('maps'):
    os.makedirs('maps')
map.save("maps/folium_exmple.html")
