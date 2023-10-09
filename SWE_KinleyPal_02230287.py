#WeatherUpdate
import requests
from geopy.geocoders import Nominatim
import time

api_key = '42e8a3c8bb719f1d2646d0feb01cde44'
api_url = 'https://api.openweathermap.org/data/2.5/weather'
token = '6661980471:AAF1QxOEPUGPADjEK9lugw48nK04jki7MYY'
chat_id = '-1001691378617'

# Function to get user's current location
def get_current_location():
    
    try:
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.geocode("")
        return location
    except Exception as e:
        print("Error: Unable to get location.", str(e))
        return None

def get_weather_data(city_name, units='metric'):
    
    try:
        response = requests.get(
            url=api_url,
            params={
                'q': city_name,
                'appid': api_key,
                'units': units,
            }
        )
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print("Error: Request to the API failed.", str(e))
        return None
        
def display_weather_data(weather_data, units):

    if weather_data:
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        if units == 'imperial':
            temperature_unit = '°F'
            wind_speed_unit = 'mph'
        else:
            temperature_unit = '°C'
            wind_speed_unit = 'm/s'

        print("Weather in {}: {}".format(city_name, description))
        print("Temperature: {}{}".format(temperature, temperature_unit))
        print("Humidity: {}%".format(humidity))
        print("Wind Speed: {} {}".format(wind_speed, wind_speed_unit))

def notofication_weather(weather_data, token, chat_id):
    message = f"Weather: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°C, Humidity: {weather_data['main']['humidity']}%, Wind Speed: {weather_data['wind']['speed']} m/s"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    time.sleep(1)
    print(requests.get(url).json())

# Main program
current_location = get_current_location()

if current_location:
    city_name = current_location.address.split(",")[-3].strip()
    print("Current Location:", city_name)
    weather_data = get_weather_data(city_name)
    if weather_data:
        display_weather_data(weather_data, units='metric')
        notofication_weather(weather_data, token, chat_id)
else:

    city_name = input("Enter the name of the city: ")
    weather_data = get_weather_data(city_name)
    if weather_data:
        units = input("Choose units (metric/imperial): ").lower()
        display_weather_data(weather_data, units=units)
        notofication_weather(weather_data, token, chat_id)

#import the necessary libraries:
# The code first imports the following two libraries:
# requests: This library is used to send HTTP requests to the OpenWeatherMap API in order to retrieve weather information.
# Taken verbatim from geopy.geocoders: Based on the user's IP address, it is utilized for geolocation to determine the user's present location.

#The script begins by defining the OpenWeatherMap API key and URL. 
# Set API Key and API URL: # The script begins by defining the OpenWeatherMap API key and URL. Substitute your real OpenWeatherMap API key for api_key.

# Definition of Functions
# get_current_location(): Based on the user's IP address, this method utilizes the Nominatim geocoder to ascertain their current location. It gives back the location data in the form of an object.
#The method get_weather_data(city_name, units='metric') accepts a city name as well as an optional unit type (the default is metric). To obtain weather information for the chosen city, it performs an HTTP GET request to the OpenWeatherMap API. As a JSON object, the weather information is returned.
# display_weather_data(weather_data, units): This function shows the weather data, including description, temperature, humidity, and wind speed, in the selected units (metric or imperial), depending on the provided weather data and unit type.

#The primary program is:The get_current_location() method is used at the beginning of the main program to try to determine the user's current location. If it is successful, it outputs "Current Location: [city_name]" after extracting the city name from the location object.
# The get_weather_data() method is then used with the name of the discovered city to retrieve weather information.
# The application asks the user to manually input a city name if the present location cannot be determined or if there is a problem retrieving weather information.
# The user is given the option to select between metric and imperial units for temperature and wind speed after receiving meteorological data.
# In order to display the weather data in the selected units, it calls the display_weather_data() method last.

# This code offers users a straightforward command-line interface via which they may manually input a city name or use their current location to receive weather information. It also provides temperature and wind speed unit customisation.