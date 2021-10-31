import folium


class SwissMap:
    def __init__(self) -> None:
        self.m = folium.Map(location=[46.8132, 8.2242], tiles='OpenStreetMap', zoom_start=6.5, min_zoom = 6, max_zoom = 12)
    

    # Returns travel map of customer as html string
    def travel_history_map(self, customer_id, travel_history):
        local_m = self.m

        counter = 0 # introduce counter for better overview 
        for e in travel_history:
            counter += 1
            if counter > 5:
                break
            place, coordinates = e.location_name, e.location_coordinates
            folium.Marker(
                location=coordinates, # coordinates for the marker
                popup=place, # pop-up label for the marker
                icon=folium.Icon(color="red")
            ).add_to(local_m)
        local_m.save(f'static/travelhistorymap_customer{customer_id}.html')
        return(f'static/travelhistorymap_customer{customer_id}.html')


    # own_location and destination are tuples in form (coordinates, place)
    def destination_map(self, customer_id, own_location, destination):
        local_m = self.m
        folium.Marker(
            location=own_location[1], # coordinates for the marker
            popup=own_location[0], # pop-up label for the marker
            icon=folium.Icon(color="blue")
        ).add_to(local_m)
        folium.Marker(
            location=destination[1], # coordinates for the marker
            popup=destination[0], # pop-up label for the marker
            icon=folium.Icon(color="red")
        ).add_to(local_m)
        local_m.save(f'static/destinationmap_customer={customer_id}_destination{destination[0]}.html')
        return(f'static/destinationmap_customer={customer_id}_destination{destination[0]}.html')
        


# Working examples for travel history map and destination map
"""
# Hard coded location list
location_list = [('Center of Switzerland' , [46.8132, 8.2242]), ('Zermatt', [46.11654, 7.445683])]
customer_id = 235

# Travel history
thmap = SwissMap()
thmap.travel_history_map(customer_id, location_list)

# Destination
dmap = SwissMap()
dmap.destination_map(customer_id, location_list[0], location_list[1])
"""