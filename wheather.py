'''
Create a script called weather that return the environmental parameters (temperature
(min, max), windspeed, humidity, cloud, pressure, sunrise and sunset)
of any location you want; after passing arguments (like user api and city id)
'''
import requests, json
import datetime
def script():
    api_key = "1ef76078cdc8fe511422e24b6f24b0e2"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = input("Enter city name(hyderabad/pune) : ")

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()
    if x["cod"] != "404":
        sun = list()

        y = x["main"]

        current_temperature = y["temp"]
        max_temp = y["temp_max"]
        min_temp = y["temp_min"]

        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        sw = x["sys"]
        sun.append(sw["sunrise"])
        sun.append(sw["sunset"])
        speed = x["wind"]["speed"]

        sun[0] = datetime.datetime.fromtimestamp(sun[0])
        sun[1] = datetime.datetime.fromtimestamp(sun[1])

        weather_description = z[0]["description"]
        return current_temperature,max_temp,min_temp,current_pressure,sun,speed,current_humidiy,weather_description
        # print following values
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n Maximum Temperature = " + str(max_temp) +
              "\n Minimum Temperature = " + str(min_temp) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n Sunrise time = " + str(sun[0]) +
              "\n Sunset time = " + str(sun[1]) +
              "\n Windspeed =" + str(speed) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))

    else:
        print(" City Not Found ")

current_temperature,max_temp,min_temp,current_pressure,sun,speed,current_humidiy,weather_description=script()
print(" Temperature (in kelvin unit) = " +str(current_temperature) +
              "\n maximum temperature = " + str(max_temp) +
              "\n minimum temperature = " + str(min_temp) +
              "\n atmospheric pressure (in hpa unit) = " +
              str(current_pressure) +
              "\n sunrise time = " + str(sun[0]) +
              "\n sunset time = " + str(sun[1]) +
              "\n windspeed =" + str(speed) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))