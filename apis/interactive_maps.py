import folium
from folium import plugins
import json

#OpenStreetMap
m = folium.Map(location=[46.8132, 8.2242], tiles='CartoDB', zoom_start=7.6, min_zoom = 6, max_zoom = 12)


# Hard coded location list
location_list = [('Center of Switzerland' , [46.8132, 8.2242]), ('Zermatt', [46.11654, 7.445683])]

for place, coordinates in location_list:
    folium.Marker(
        location=coordinates, # coordinates for the marker
        popup=place, # pop-up label for the marker
        icon=folium.Icon(color="red")#, icon_color = 'red', icon="fa-map-marker-alt", prefix='fa')
    ).add_to(m)


m.save('foliummap.html')

html_string = m.get_root().render()
print(html_string)
print('finish')

return html_string