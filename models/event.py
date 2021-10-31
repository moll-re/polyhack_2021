from .travel_route import TravelRoute

class Event:
    id = 0
    name = ""
    location_name = []
    location_coordinates = []
    description = ""
    reviews = []
    category = []
    weather_requirements = 0
    date = ""
    image_path = "fallback.jpg"
    activity_duration = "" # datetime object
    trip_to = TravelRoute(0,0)
    trip_back = TravelRoute(0,0)

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id")
        self.name = kwargs.pop("name")
        self.location_name = kwargs.pop("location_name")
        self.location_coordinates = kwargs.pop("location_coordinates")
        self.date = kwargs.pop("date")
        self.description = kwargs.pop("description")
        self.activity_duration = kwargs.pop("activity_duration")
        self.image_path = kwargs.pop("image_path")

    
    def find_optimal_trip(self):
        pass
    
    def add_review(self, **kwargs):
        self.reviews.append(Review(**kwargs))


    @property
    def trip_is_good(self):
        pass

    @property
    def co2_savings(self):
        return self.trip_to.co2_savings + self.trip_back.co2_savings
        
    @property
    def rating(self):
        return int(sum([r.rating for r in self.reviews]) / len(self.reviews))

    @property
    def nreviews(self):
        return len(self.reviews)

    @property
    def total_duration(self):
        s = (self.activity_duration + self.trip_back.duration + self.trip_to.duration).seconds
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02} h {:02}'.format(int(hours), int(minutes))




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
        for e in self._events:
            if e.id == id:
                return e
        return None

    def __iter__(self):
        return iter(self._events)