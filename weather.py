import requests
# import location
import json

def get_weather(loc):

    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    # loc = location.get_location()
    querystring = {"q":loc["location"],"lat":"0","lon":"0","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

    headers = {
        'x-rapidapi-key': "232ca168b2msh67264d324a19c26p156a31jsnc112743d858a",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(response.text)
    weather = response["weather"]
    main = weather[0]
    weather = {}
    weather["ac"] = main["main"]
    weather["desc"] = main["description"]
    return weather

# print(get_weather())