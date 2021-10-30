import tortilla
import requests


def get_auth():
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



SBB = tortilla.wrap('https://b2p-int.api.sbb.ch/api')
SBB.config.headers = get_auth()
# SBB.config.headers = {
#     "grant_type" : "client_credentials",
#     "client_secret" : "ae61e214f679558c28678d5c638c5725",
#     "client_id" : "af929f08pied!",
# }


# Authorization: Bearer $accessToken' \
#  ​-H 'Cache-Control: no-cache' \
#  ​-H 'Accept: application/json' \
#  ​-H 'X-Contract-Id: ABC1234' \
#  ​-H 'X-Conversation-Id: e5eeb775-1e0e-4f89-923d-afa780ef844b


loc = SBB.locations
print(loc.get(params = {"name":"Bern"}))