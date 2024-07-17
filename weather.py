# it is pre-function for get weatger data
import requests
from dotenv import load_dotenv
import os


# getting api key 
load_dotenv()
api = os.getenv('WEATHER_API')

def get_location_by_ip():
    # getting ip address
    ip = requests.get('https://api.ipify.org').text

    # getting location data by ip address
    response = requests.get(f'http://ip-api.com/json/{ip}')

    # converting response to json format
    location_data = response.json()

    return location_data

def weather_data(location_data):
    # getting coordinats from get_location_by_ip()
    lat = location_data['lat']
    lon = location_data['lon']

    # parsing web page of openweathermap
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric&lang=ru"
    response  = requests.get(api_url)
    return response.json()

def weather_output():
    location_data = get_location_by_ip()
    weather_info = weather_data(location_data)
    weather = f'В населённом пункте {weather_info['name']} сейчас {weather_info['weather'][0]['description']}, {int(weather_info['main']['temp'])} °C, ощущается как {int(weather_info['main']['feels_like'])} °C'
    print(weather)
    return weather

