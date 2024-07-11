# it is pre-function for get weatger data
import requests

# getting api key from file
with open(r"C:\Users\reyst\Desktop\практика\кое-что\weather_api.txt", 'r') as f:
    api = f.read().strip()

def get_location_by_ip():
    # getting ip address
    ip = requests.get('https://api.ipify.org').text

    # getting location data by ip address
    response = requests.get(f'http://ip-api.com/json/{ip}')

    # converting response to json format
    location_data = response.json()

    return location_data

def weather_data():
    # getting coordinats from get_location_by_ip()
    lat = get_location_by_ip()['lat']
    lon = get_location_by_ip()['lon']

    # parsing web page of openweathermap
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric&lang=ru"
    response  = requests.get(api_url)
    return response.json()

def weather_output():
    weather_data()
    weather = f'В населённом пункте {weather_data()['name']} сейчас {weather_data()['weather'][0]['description']}, {int(weather_data()['main']['temp'])} °C, ощущается как {int(weather_data()['main']['feels_like'])} °C.'
    print(weather)
    return weather
