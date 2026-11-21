import requests

city = input("Enter a city: ")
url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name" : city, "count": 1}

response = requests.get(url, params=params)
data =  response.json()

if "results" not in data:
    print(f"Couldn't find a city called {city}")
    exit()

place = data["results"][0]

name = place["name"]
country = place["country"]
latitude = place["latitude"]
longitude = place["longitude"]

print(f"Found {name}, {country} at {latitude}, {longitude}")