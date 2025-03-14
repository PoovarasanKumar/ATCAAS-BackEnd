import json

import requests
from Auth import authenticate_user 
from Agents.CommonAgent import Get_Output

def Get_TestCasesFromUserStory(Input):
    
    result =  Get_Output(Input, 'testcase-generation')
    return result.json()['message']

