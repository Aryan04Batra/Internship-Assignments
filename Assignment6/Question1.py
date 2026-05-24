#https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8a010054a996a8a5927d017258522e9b
#https://api.openweathermap.org/data/2.5/weather?q=jaipur&appid=8a010054a996a8a5927d017258522e9b
import requests
def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8a010054a996a8a5927d017258522e9b&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data= response.json()
        nested=data["main"]
        for key, value in nested.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        print(e)
city=input("Enter city name:")
weather_data(city)
