import json
import requests
from googleapiclient.discovery import build

weather_api_key = "59aca0d5837dad8c55aff93a6e3a5f28"

def get_weather(location):
    URL_weather = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={weather_api_key}"
    x = requests.get(URL_weather)
    data = x.json()
   
    if data.get("cod") != 200:
        return {"error": data.get("message", "City not found")}

    weather_info = {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    
    }
   
     
    return weather_info
    
def get_forecast(location):
    URL_weather = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={weather_api_key}"
    x = requests.get(URL_weather)
    data = x.json()
    if data.get("cod") != "200":
        return {"error": data.get("message", "City not found")}, 404

    forecast_list = []
    for x in data["list"]:
        forecast_info = {
            "date": x["dt_txt"],
            "temperature": x["main"]["temp"],
            "description": x["weather"][0]["description"],
            "humidity": x["main"]["humidity"],
            "wind_speed": x["wind"]["speed"],
        }
        forecast_list.append(forecast_info)
    forecast= [row for row in forecast_list if row["date"].endswith("12:00:00")]
    

    return forecast