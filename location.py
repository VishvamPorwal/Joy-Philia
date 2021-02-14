import requests
import json

def get_location():

    url = "http://api.ipstack.com/check?access_key=api_key"


    response = requests.request("GET", url)
    # print(response.text)
    response = json.loads(response.text)
    ip = response["ip"]
    city = response["city"]
    lat = response["latitude"]
    lon = response["longitude"]
    country = response["country_name"]
    result = {}
    result["ip"] = ip
    result["location"] = city+','+country
    result["latlon"] = str(lat)+','+str(lon)
    return result

# get_location()
