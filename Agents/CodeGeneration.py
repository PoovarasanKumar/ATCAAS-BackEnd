import json

import requests
from Auth import authenticate_user 
from Agents.CommonAgent import Get_Output

def Get_Code(Input):
    
    result = Get_Output(Input, 'robot-script-generation')
    print(result.json()['message'])

    return result.json()['message']



    # Removing the ```json and ``` from the message content
    message_content = result.json()['message'].strip('```json\n').strip('\n```')

    # Parsing the JSON content
    parsed_content = json.loads(message_content)

    # Extracting Flow and Code sections
    flow_section = parsed_content.get("Flow", {})
    code_section = parsed_content.get("Code", ":")