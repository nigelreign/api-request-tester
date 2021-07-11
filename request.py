import requests
import json
from random import randint

# enter ur api url
api_url = ""

i = 0 
while i < 100000:
    national_id = "56-74451125K" + str(randint(0, 999999))
    
    # create ur payload
    user_payload = {
    "national_id": national_id,
    "name": "Nigel",
    "last_name":"Zulu",
    }
    
    # Your api headers
    options = {
    "Content-Type": "application/json",
    "key": "*****",
    "api-username":"****",
    "api-password": "******",
    
    }

    api_response = requests.post(
    api_url, json.dumps(user_payload), headers=options
    )
    i=i+1
    print(f"Iteration {i}")

    print(api_response.json())
