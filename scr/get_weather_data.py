import requests

API_KEY = "22c68fcbf882afa9dd2ef890706bfeee"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

cities = ['Sydney', 'Melbourne', 'Brisbane', 'Perth']

def get_weather(city):
    params = {
        'q': city + ',AU',
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es'
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'ciudad': city,
            'temperatura': data['main']['temp'],
            'clima': data['weather'][0]['description']
        }
    else:
        print(f"❌ Error {response.status_code} al obtener clima para {city}")
        print(response.text)  # 👈 esto te dice el motivo
        return None


def get_all_weather(cities):
    results = []
    for city in cities:
        weather = get_weather(city)
        if weather:
            results.append(weather)
    return results

if __name__ == "__main__":
    for city in cities:
        info = get_weather(city)
        if info:
            print(info)
