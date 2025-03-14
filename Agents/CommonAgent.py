import json
import os

import requests
from Auth import authenticate_user 
from cookies import generate_cookies

def Get_Output(input,assistant_id):

    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    generate_cookies()

    authenticate_user_path = os.path.join(script_dir, '..', 'authentication.json')
    cookies_path = os.path.join(script_dir, '..', 'cookies.json')

    with open(authenticate_user_path, 'r', encoding='utf-8') as f:
        authentication = json.loads(json.load(f))

    with open(cookies_path, 'r', encoding='utf-8') as f:
        cookies = json.loads(json.load(f))


    access_token = authentication['access_token']

    

    #assistant_id = 'tt-promt-2-code'       # If you have a custom agent, add name here, else skip this

    print(assistant_id)

    model = 'gpt-4o'                                # Select from [gpt-3.5-turbo, gpt-4, gpt-4o]
    session_id =  cookies['session_id']            # If you want to have/continue a great conversation with LLM, do not change
    interlocutor_id = cookies['interlocutor_id']   # This is your unique ID as a user, never change
    # session_id =  'd1'            # If you want to have/continue a great conversation with LLM, do not change
    # interlocutor_id = 'd1'
    stream = False                                 # Set to False if you can wait for a while, else True if your want WIP response

    message = input                     # Add your message here
    print(message)

    url = "https://agw.construction-integration.trimble.cloud/trimbledeveloperprogram/assistants/v1/agents/{assistant_id}/messages".format(assistant_id=assistant_id)   

    headers = {
        'Authorization': 'Bearer {access_token}'.format(access_token=access_token),
        'Content-Type': 'application/json'
    }

    body = {
        "message": message,
        "session_id": session_id,
        "interlocutor_id": interlocutor_id,
        "stream": stream,
        "model_id": model
    }

    #print(message)

    try:
        response = requests.post(url, 
                                headers=headers, 
                                data=json.dumps(body))
        
    except Exception as e:
        #auth_response = authenticate_user()
        try:
            response = requests.post(url, 
                            headers=headers, 
                            data=json.dumps(body))
        except Exception as e:
            return str(e)

    print(response.json())

    return response       # The response you seek is here

    return response.json()['message']          # The response you seek is here

