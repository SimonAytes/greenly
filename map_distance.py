import openrouteservice
from openrouteservice import convert
import folium
import json

client = openrouteservice.Client(key='5b3ce3597851110001cf624877c925483b25437bb5377f967eccb8d7')

coords = ((-97.7237614,30.4027446),(-97.7517604,30.2659279))
res = client.directions(coords)
geometry = client.directions(coords)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

distance_txt = "<b>Distance " + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000 * 0.62137,1))+" Miles || </strong>" +"</b>"
duration_txt = "<b>Duration " + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</b>"

m = folium.Map(location=[30.4027446,-97.7237614],zoom_start=11, control_scale=True)
folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=250)).add_to(m)

folium.Marker(
    location=list(coords[0][::-1]),
    popup="Aloft Austin at The Domain",
    icon=folium.Icon(color="lightgreen"),
).add_to(m)

folium.Marker(
    location=list(coords[1][::-1]),
    popup="Austin Central Library Special Events Center",
    icon=folium.Icon(color="green"),
).add_to(m)
m

