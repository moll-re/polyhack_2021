import folium


class SwissMap:
    def __init__(self) -> None:
        self.m = folium.Map(location=[46.8132, 8.2242], tiles='OpenStreetMap', zoom_start=7.6, min_zoom = 6, max_zoom = 12)
    
    
    # Returns travel map of customer as html string
    def customer_map(self, customer_id, location_list):
        local_m = self.m
        for place, coordinates in location_list:
            folium.Marker(
                location=coordinates, # coordinates for the marker
                popup=place, # pop-up label for the marker
                icon=folium.Icon(color="red")#, icon_color = 'red', icon="fa-map-marker-alt", prefix='fa')
            ).add_to(local_m)
        local_m.save(f'static/swissmap_customer={customer_id}.html')
        return(f'static/swissmap_customer={customer_id}.html')


# Working example
"""
# Hard coded location list
location_list = [('Center of Switzerland' , [46.8132, 8.2242]), ('Zermatt', [46.11654, 7.445683])]
customer_id = 235

cmap = SwissMap()
cmap.customer_map(customer_id, location_list)
"""
