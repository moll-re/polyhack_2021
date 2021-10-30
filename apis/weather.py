import tortilla
import requests

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

        #response = requests.post('https://sso-int.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token', data=token_query).json()
        response = requests.post('https://sso.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token', data=token_query).json()
        token = response["access_token"]
        auth = {
            'Authorization': f"Bearer {token}",
            'X-Contract-Id': 'PLY223P',
            # 'X-Conversation-Id': str(conv_id),
        }
        return auth

weather = WeatherWrapper()
print('TEST')
print(weather.wrapper.get('2021-07-12T00:00ZP50D:PT30M/sfc_pressure:hPa,msl_pressure:hPa/47.36669,8.54858+47.35209,7.90779/json'))