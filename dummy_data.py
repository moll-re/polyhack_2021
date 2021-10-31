import datetime

def populate_data(Users, Events):
    Events.add_event(
        id = 1, 
        location_name = 'Center of Switzerland',
        location_coordinates = [46.8132, 8.2242],
        date = datetime.date.today() - datetime.timedelta(days=100)
        )
    Events.add_event(
        id = 2, 
        location_name = 'Center of Switzerland',
        location_coordinates = [46, 8],
        date = datetime.date.today() - datetime.timedelta(days=1)
        )
    Events.add_event(
        id = 3, 
        location_name = 'Center of Switzerland',
        location_coordinates = [46.8132, 9],
        date = datetime.date.today() - datetime.timedelta(days=2)
        )
    Events.add_event(
        id = 4, 
        location_name = 'Center of Switzerland',
        location_coordinates = [47, 8.2242],
        date = datetime.date.today() - datetime.timedelta(days=3)
        )
    Events.add_event(
        id = 5, 
        location_name = 'Center of Switzerland',
        location_coordinates = [40.8132, 8.2242],
        date = datetime.date.today() - datetime.timedelta(days=56)
        )
    Events.add_event(
        id = 6,
        location_name = 'Zermatt',
        location_coordinates = [46.11654, 10.445683],
        date = datetime.date.today()
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
        u.travel_history.append(e)
    
