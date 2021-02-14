import requests
import json

def get_greet(loc):

    url = "https://fourtonfish.com/hellosalut/"
    querystring = {"ip":loc["ip"]}
    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    
    return response

# print(get_greet())