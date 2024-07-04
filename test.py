#здесь пробная функция для получения данных о погоде
import requests

def get_location_by_ip():
    # Получение IP-адреса
    ip = requests.get('https://api.ipify.org').text

    # Получение местоположения по IP
    response = requests.get(f'http://ip-api.com/json/{ip}')

    # Преобразование ответа в JSON
    location_data = response.json()

    return location_data

def get_weather_data():
    api_key = 'cd358e39ad85a24a6cb8cce854b27b0f'
    lat = get_location_by_ip()['lat']
    lon = get_location_by_ip()['lon']
    api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    response  = requests.get(api_url)
    return response.json()

print(get_weather_data())