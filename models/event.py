
class Event:
    coordinates = []
    reviews = []
    category = []
    weather_requirements = 0

    trip_to = ""
    trip_back = ""

    def __init__(self, **kwargs):
        pass

    
    def find_optimal_trip(self):
        pass

    @property
    def trip_is_good(self):
        pass



class Review:
    text = ""
    rating = 0 # max 5
    additional_photos = []


    def __init__(self, text, rating) -> None:
        self.text = text
        self.rating = rating


    def add_photo(self, photo):
        pass


