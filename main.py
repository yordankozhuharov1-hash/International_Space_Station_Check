import requests
from datetime import datetime
import os

MY_LAT = 42.71293061932975
MY_LONG = 23.37905216990742

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sun_data = response.json()

sunrise = sun_data["results"]["sunrise"].split("T")[1]
sunset = sun_data["results"]["sunset"].split("T")[1]

time_now = datetime.now()

#If the ISS is close to my current position
#And it's currently dark
if 37<=iss_lat<48 and 18<=iss_long<28:
    if time_now.hour >= int(sunset.split(":")[0]) or time_now.hour <= int(sunrise.split(":")[0]):
        os.system('msg * "The ISS is above you in the sky."')
else:
    os.system('msg * "The ISS is not above you."')