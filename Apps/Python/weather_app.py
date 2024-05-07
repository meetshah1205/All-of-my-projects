import requests

print("**************************")
print("*   WeLCOME TO WEATHERER *")
print("**************************")

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change units to imperial for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to retrieve weather data.")

# Enter your OpenWeatherMap API key here
api_key = "6f41a3e6754129f2ff59ea2dc86018f8"
# Get the city name from the user
city = input("Enter city name: ")
get_weather(city, api_key)


