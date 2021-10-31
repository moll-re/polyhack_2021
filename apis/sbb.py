import tortilla
import requests


class SBBWrapper:
    def __init__(self) -> None:
        self.wrapper = tortilla.wrap('https://b2p-int.api.sbb.ch/api')
        self.wrapper.config.headers = self.get_auth() 


    
    def get_auth(self):
        token_query = {
            'grant_type': 'client_credentials',
            'client_id': 'af929f08',
            'client_secret': 'ae61e214f679558c28678d5c638c5725'
        }

        response = requests.post('https://sso-int.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token', data=token_query).json()

        token = response["access_token"]
        auth = {
            'Authorization': f"Bearer {token}",
            'X-Contract-Id': 'PLY223P',
            # 'X-Conversation-Id': str(conv_id),
        }
        return auth


sbb = SBBWrapper()
print(sbb.wrapper.get('route-offers'))


"""
tripQuery = {
    'date' : '2021-10-31',
    'time' : '19:44',
    'originId' : "8591122",
    'destinationId' : "8591123",
}

sbb = SBBWrapper()
print(sbb.wrapper.trips.get(params=tripQuery))
"""

"""
#Example for locations
query = {'name':'Kreuzlingen'}

sbb = SBBWrapper()
print(sbb.wrapper.locations.get(params=query))
"""