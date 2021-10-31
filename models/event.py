
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
    duration = "" # datetime object
    trip_to = "" # Trip object
    trip_back = ""

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id")
        self.name = kwargs.pop("name")
        self.location_name = kwargs.pop("location_name")
        self.location_coordinates = kwargs.pop("location_coordinates")
        self.date = kwargs.pop("date")
        self.description = kwargs.pop("description")

    
    def find_optimal_trip(self):
        pass
    
    def add_review(self, **kwargs):
        self.reviews.append(Review(**kwargs))


    @property
    def trip_is_good(self):
        pass

    @property
    def co2_savings(self):
        try:
            return self.trip_to.co2_savings + self.trip_back.co2_savings
        except:
            return 5
    @property
    def rating(self):
        return int(sum([r.rating for r in self.reviews]) / len(self.reviews))

    @property
    def nreviews(self):
        return len(self.reviews)


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