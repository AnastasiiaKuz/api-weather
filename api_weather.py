import requests as rqs

endpoint = "https://api.openweathermap.org/data/2.5/onecall" #before ?-mark
api_key = "1e9e97b4f67c9523191c6b2f18d2914b"
lat = 60.324535
lon = 5.265803

parameters={
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

# https://api.openweathermap.org/data/2.5/onecall?lat=60.324535&lon=5.265803&appid=1e9e97b4f67c9523191c6b2f18d2914b - doesn't work
# https://api.openweathermap.org/data/2.5/weather?lat=60.324535&lon=5.265803&appid=1e9e97b4f67c9523191c6b2f18d2914b - works

response = rqs.get(endpoint, params=parameters)
response.raise_for_status()

data = response.json()
print(data)