import os
from uuid import uuid4
import json

def generate_cookies():
    client_id = "e469485d-8c6f-4e82-ac9d-47085fb8d9f6"
    interlocutor_id =  os.environ.get(client_id)
    session_id = uuid4()

    cookies = {
        "interlocutor_id": interlocutor_id,
        "session_id": session_id.__str__()
    }

    with open('cookies.json', 'w', encoding='utf-8') as f:
        json.dump(json.dumps(cookies), f)