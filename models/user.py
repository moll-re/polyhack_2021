class User:
    id = 0
    name = ""
    event_preferences = []
    event_blacklist = []
    home_coordinates = []
    group_size = 0
    min_age = 0
    max_age = 0
    travel_history = [] # (Name, coordinates)
    co2_savings = []
    
    def __init__(self, **kwargs):
        self.id = kwargs.pop("id")
        self.name = kwargs.pop("name")
        self.home_coordinates = kwargs.pop("home_coordinates")
        self.event_preferences = kwargs.pop("event_preferences")
        self.event_blacklist = kwargs.pop("event_blacklist")
        self.group_size = kwargs.pop("group_size")
        self.min_age = kwargs.pop("min_age")
        self.max_age = kwargs.pop("max_age")


    @property
    def number_of_trips(self):
        return len(self.travel_history)
    
    @property
    def total_co2_savings(self):
        return sum(self.co2_savings)

    
class Users:
    _users = []

    def add_user(self, **kwargs):
        self._users.append(User(**kwargs))

    def get_by_id(self, id):
        for u in self._users:
            if u.id == id:
                return u