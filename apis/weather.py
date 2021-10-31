import tortilla
import requests
import numpy as np
import datetime


class WeatherWrapper:
    def __init__(self) -> None:
        self.wrapper = tortilla.wrap('https://weather.api.sbb.ch/')
        self.wrapper.config.headers = self.get_auth() 
    
    def get_auth(self):
        token_query = {
            'grant_type': 'client_credentials',
            'client_id': '56bae62c',
            'client_secret': '59603134536c874e47245b4de403e3d3'
        }

        response = requests.post('https://sso.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token', data=token_query).json()
        token = response["access_token"]
        auth = {
            'Authorization': f"Bearer {token}",
            'X-Contract-Id': 'PLY223P',
            # 'X-Conversation-Id': str(conv_id),
        }
        return auth


class WeatherScoreCalculator:
    def calc_weather_score(self, event):
        now = (datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=1)).isoformat()
        location = event.location_coordinates
        location_string = f'{location[0]}'+f','+f'{location[1]}'

        weather = WeatherWrapper()
        raw_weather_data = weather.wrapper.get( now + 'ZP1D:PT3H/weather_code_6h:idx/'+ location_string + '/json')
        raw_extracted_weather = raw_weather_data['data'][0]['coordinates'][0]['dates']

        # Weather Score Calculation
        weather_score = []
        for weather_dict in raw_extracted_weather:
            weather_score.append(weather_dict['value'])
        weather_score = np.array(weather_score)
        mean_weather_score = weather_score.mean()

        return mean_weather_score


# Example. Event is an event object, (not defined in this file).
"""
wcalc = WeatherScoreCalculator()
print(wcalc.calc_weather_score(event))
"""


# Obsolete
"""
now = datetime.datetime.now().replace(microsecond=0).isoformat()

weather = WeatherWrapper()
raw_weather_data = weather.wrapper.get( now + 'ZP1D:PT3H/weather_code_6h:idx/47.36669,8.54858/json')
raw_extracted_weather = raw_weather_data['data'][0]['coordinates'][0]['dates']

print(now)
print(raw_extracted_weather)

# Weather Score Calculation
weather_score = []
for weather_dict in raw_extracted_weather:
    weather_score.append(weather_dict['value'])
weather_score = np.array(weather_score)
mean_weather_score = weather_score.mean()
print(mean_weather_score)
"""