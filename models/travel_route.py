# TBD API interaction

import datetime


class TravelRoute:
    def __init__(self, start_coords, end_coords) -> None:
        pass
    
    @property
    def duration(self):
        return datetime.timedelta(hours=2)

    @property
    def wait_time(self):
        return datetime.timedelta(minutes=10)
        

    @property
    def co2_savings(self):
        return 15