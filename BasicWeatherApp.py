import requests

def get_weather(city):
    api_key = "a2c59cb2e81ef9a12ab7b141eb042ec3"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params={
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        condition = weather['description']
        print(f"\nWeather in City: {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("\nCity Not Found!.please check the name and try again.")
city_name = input("Enter city name: ")
get_weather(city_name)