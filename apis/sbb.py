import tortilla
import requests
import pandas as pd


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
"""
sbb=SBBWrapper()
print(sbb.wrapper.get('name':'Bern'))
"""

"""
header_dict = {'api_key' : '814d86a3ffc49c350bb7dcc48cac69b3'}

response =  requests.get('https://journey-maps.api.sbb.ch:443', headers=header_dict)
print(response.text)
"""


"""
header_dict = {'api_key' : 'xxxxx'}
response = requests.get('https://journey-pois-int.api.sbb.ch/', headers=header_dict)
print(response)

"""
""""

header_dict = {'key':'yourtest-outdoora-ctiveapi',
'project' : 'api-dev-oa' }
response = requests.get('http://www.outdooractive.com/api', headers=header_dict).json()
print(response)
print('finish')
"""