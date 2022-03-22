import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("My_API_Key")
account_sid = os.getenv("My_API_ACCT")
auth_token = os.getenv("My_Auth_Token")



parameters = {
    "lat" : 33.753746,
    "lon" : -84.386330,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False
response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data)

for num in range(12):
    if (int(weather_data["hourly"][num]["weather"][0]['id'])) < 700:
        will_rain = True

if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages \
    .create(
       body="It's going to rain today. Remember to  bring a rain jacket",
       from_="+19495758903",
       to= os.getenv("My_Cell")
   )

