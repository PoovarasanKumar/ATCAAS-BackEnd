import json

import requests
from Auth import authenticate_user 
from Agents.CommonAgent import Get_Output

def Get_TestData(Input):
    
    result = Get_Output(Input, 'generate-testdata')
    return  result.json()['message']
