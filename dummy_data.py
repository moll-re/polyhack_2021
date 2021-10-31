import datetime
import random

def populate_data(Users, Events):
    Events.add_event(
        id = 1,
        name = "Polyhack 2021",
        location_name = 'SPH Zentrum, Zürich',
        location_coordinates = [46.3667, 7.445683],
        date = datetime.date.today() - datetime.timedelta(days=100),
        description = "Be part of Switzerland's most fun and personal hackathon experience!"
        )
    Events.add_event(
        id = 2,
        name = "Swiss National Museum Zürich",
        location_name = 'Zürich',
        location_coordinates = [46.368, 7.445683],
        date = datetime.date.today() - datetime.timedelta(days=80),
        description = "Explore Switzerland's rich cultural history in the unique collection of the Swiss National Museum."
        )
    Events.add_event(
        id = 3,
        name = "Paragliding in Interlaken",
        location_name = 'Interlaken',
        location_coordinates = [46.68387, 7.86638],
        date = datetime.date.today() - datetime.timedelta(days=100),
        description = "Fly high between the lakes in Interlaken."
        )
    Events.add_event(
        id = 4,
        name = "City Tour Lugano",
        location_name = 'Lugano',
        location_coordinates = [46.01008, 8.96004],
        date = datetime.date.today() - datetime.timedelta(days=100),
        description = "Explore one of Ticino's gems in the deep south of Switzerland."
        )
    Events.add_event(
        id = 5,
        name = "City Tour Lucerne",
        location_name = 'Lucerne',
        location_coordinates = [47.05048, 8.30635],
        date = datetime.date.today() - datetime.timedelta(days=20),
        description = "See the iconic bridge of Lucerne and enjoy a boat tour on the Vierwaldstätter Lake."
        )
    Events.add_event(
        id = 6,
        name = "Hike at Oeschinen Lake",
        location_name = 'Oeschinen Lake',
        location_coordinates = [46.492331364, 7.722830442],
        date = datetime.date.today(),
        description = "Take a hike around the beautiful scenery around the Oeschinen Lake."
        )
    Events.add_event(
        id = 7,
        name = "Hike at Aletschglacier",
        location_name = 'Aletschglacier',
        location_coordinates = [46.438664912, 8.072999708],
        date = datetime.date.today(),
        description = "Be adventurous by hiking the largest Glacier of the Alps."
        )
    Events.add_event(
        id = 8,
        name = "Ski at Engelberg",
        location_name = 'Engelberg',
        location_coordinates = [46.82107, 8.40133],
        date = datetime.date.today(),
        description = "Enjoy a Ski weekend at the Engelberg Ski Resort."
        )
    Events.add_event(
        id = 9,
        name = "City Tour Davos",
        location_name = 'Davos',
        location_coordinates = [46.80429, 9.83723],
        date = datetime.date.today(),
        description = "See the winter wonderous municipality Davos in East Switzerland."
        )
    Events.add_event(
        id = 10,
        name = "Zermatt",
        location_name = 'Zermatt',
        location_coordinates = [46.11654, 7.445683],
        date = datetime.date.today() - datetime.timedelta(days=10),
        description = "Enjoy skiing with view on one of Switzerland's most iconic mountain peaks."
        )

    Users.add_user(
        id=239842123,
        name="Remy",
        event_preferences=["hiking","skiing"],
        event_blacklist = [],
        home_coordinates=[0,0],
        group_size=1,
        min_age=20,
        max_age=20,
        )
    u = Users.get_by_id(239842123)

    for e in Events[2:5]:
        e.add_review(text="Nice view, good weather. Would recommend.", rating=random.randint(4,5))
        u.travel_history.append(e)