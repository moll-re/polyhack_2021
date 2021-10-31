import datetime
import random

def populate_data(Users, Events):
    Events.add_event(
        id = 1,
        name = "a",
        location_name = 'Center of Switzerland',
        location_coordinates = [46.8132, 8.2242],
        date = datetime.date.today() - datetime.timedelta(days=100),
        description = "slkjfslkdfjsldkfjsd"
        )
    Events.add_event(
        id = 2,
        name = "b",
        location_name = 'Center of Switzerland',
        location_coordinates = [46, 8],
        date = datetime.date.today() - datetime.timedelta(days=1),
        description = "slkjfslkdfjsldkfjsd"
        )
    Events.add_event(
        id = 3,
        name = "kfkslkjdf",
        location_name = 'Center of Switzerland',
        location_coordinates = [46.8132, 9],
        date = datetime.date.today() - datetime.timedelta(days=2),
        description = "slkjfslkdfjsldkfjsd"
        )
    Events.add_event(
        id = 4,
        name = "s",
        location_name = 'Center of Switzerland',
        location_coordinates = [47, 8.2242],
        date = datetime.date.today() - datetime.timedelta(days=3),
        description = "slkjfslkdfjsldkfjsd"
        )
    Events.add_event(
        id = 5,
        name = "d",
        location_name = 'Center of Switzerland',
        location_coordinates = [40.8132, 8.2242],
        date = datetime.date.today() - datetime.timedelta(days=56),
        description = "slkjfslkdfjsldkfjsd"
        )
    Events.add_event(
        id = 6,
        name = "kfkslkjdf",
        location_name = 'Zermatt',
        location_coordinates = [46.11654, 10.445683],
        date = datetime.date.today(),
        description = "slkjfslkdfjsldkfjsd"
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

    for e in Events:
        e.add_review(text="Nice view, good weather. Would recommend.", rating=random.randint(0,5))
        u.travel_history.append(e)
    
