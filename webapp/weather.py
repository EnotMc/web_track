from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather: #Проверяем есть ли секция(словарь) в нашем результате!
            if 'current_condition' in weather['data']:#Проверяем есть ли этот список
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False

if __name__=='__main__':
    w = weather_by_city('Moscow,Russia')
    print(w)
    #print(weather_by_city('Moscow,Russia')) можно вызвать так!