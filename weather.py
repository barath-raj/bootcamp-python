

from datetime import datetime
import requests

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
place= input("Enter the name of the city: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(place.upper(), date_time))
print ("-------------------------------------------------------------")

print ("temperature is: {:.2f} deg C".format(temp_city))
print ("weather  :",weather_desc)
print ("humdidity      :",humidity, '%')
print ("speed of the wind   :",wind_speed ,'kmph')
