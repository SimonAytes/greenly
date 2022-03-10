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
folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,min_width=15,max_width=40)).add_to(m)

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

m.save('aloft_to_librery2.html')
print("DONE!")


coords = ((-97.740350,30.274665),(-97.7517604,30.2659279))
res = client.directions(coords)
geometry = client.directions(coords)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

distance_txt2 = "<b>Distance " + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000 * 0.62137,1))+" Miles || </strong>" +"</b>"
duration_txt2 = "<b>Duration " + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</b>"

m2 = folium.Map(location=[30.4027446,-97.7237614],zoom_start=11, control_scale=True)
folium.GeoJson(decoded).add_child(folium.Popup(distance_txt2+duration_txt2,min_width=15,max_width=40)).add_to(m2)

folium.Marker(
    location=list(coords[0][::-1]),
    popup="Texas state capitol building",
    icon=folium.Icon(color="lightgreen"),
).add_to(m2)

folium.Marker(
    location=list(coords[1][::-1]),
    popup="Austin Central Library Special Events Center",
    icon=folium.Icon(color="green"),
).add_to(m2)

m2

m2.save('library_to_texas_capitol.html')
print("DONE!")
