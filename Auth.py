import requests
import json
from requests.auth import HTTPBasicAuth

def authenticate_user():

    # client_id = "9b98ef93-56f4-4775-8f57-cd260c30d17c"
    # client_secret ="Shipment-Portal-Intelligent-Invoice-Processing"

    client_id = "e469485d-8c6f-4e82-ac9d-47085fb8d9f6"
    client_secret ="72a01ad5db4048af97f5d8d9ef6d4757"

    url: str = 'https://id.trimble.com/oauth/token'
    authentication = HTTPBasicAuth(client_id, client_secret)

    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    body = {
        'grant_type': 'client_credentials',
        'scope': 'MyTrimbleAssistantClient'
    }

    response = requests.post(url=url, headers=headers, auth=authentication, data=body)

    #print(response.json())

    content = {}

    content['access_token'] = response.json()['access_token']
    content['expires_in'] = response.json()['expires_in']
    content['token_type'] = response.json()['token_type']

    with open('authentication.json', 'w', encoding='utf-8') as f:
        json.dump(json.dumps(content), f)