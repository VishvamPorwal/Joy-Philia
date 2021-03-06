import requests
import json

def get_nearby(location):
    
    url = "https://trueway-places.p.rapidapi.com/FindPlacesNearby"

    querystring = {"location":location["latlon"],"radius":"1000", "type":"restaurant"}

    headers = {
        'x-rapidapi-key': "api_key",
        'x-rapidapi-host': "trueway-places.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    response = json.loads(response.text)
    response = response["results"]
    # print(response)
    return response

# get_nearby("22.719568,75.857727")
