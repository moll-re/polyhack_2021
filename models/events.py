

class User:
    name = ""
    event_preferences = []
    event_blacklist = []
    home_coordinates = []
    group_size = 0
    min_age = 0
    max_age = 0
    
    def __init__(self, **kwargs):
        self.name = kwargs.pop("name")
        self.home_coordinates = kwargs.pop("home_coordinates")
        self.event_preferences = kwargs.pop("event_preferences")
        self.event_blacklist = kwargs.pop("name")
        self.group_size = kwargs.pop("group_size")
        self.min_age = kwargs.pop("min_age")
        self.max_age = kwargs.pop("max_age")
