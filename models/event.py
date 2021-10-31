
class Event:
    id = 0
    location_name = []
    location_coordinates = []
    reviews = []
    category = []
    weather_requirements = 0
    date = ""
    
    duration = "" # datetime object
    trip_to = "" # Trip object
    trip_back = ""

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id")
        self.location_name = kwargs.pop("location_name")
        self.location_coordinates = kwargs.pop("location_coordinates")
        self.date = kwargs.pop("date")
    
    def find_optimal_trip(self):
        pass

    @property
    def trip_is_good(self):
        pass

    @property
    def co2_savings(self):
        try:
            return self.trip_to.co2_savings + self.trip_back.co2_savings
        except:
            return 5


class Review:
    text = ""
    rating = 0 # max 5
    additional_photos = []


    def __init__(self, text, rating) -> None:
        self.text = text
        self.rating = rating


    def add_photo(self, photo):
        pass

class Events:
    _events = []

    def add_event(self, **kwargs):
        self._events.append(Event(**kwargs))

    def get_by_id(self, id):
        for e in self.events:
            if e.id == id:
                return e

    def __iter__(self):
        return iter(self._events)