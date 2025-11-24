from flask import Flask, request, jsonify, send_from_directory
from Weather import get_weather, get_forecast

app = Flask(__name__, static_folder='static')

@app.get("/")
def home():
    return send_from_directory('static', 'index.html')

@app.get("/weather")
def weather_api():
    location = request.args.get("city")
    return jsonify(get_weather(location))

@app.get("/forecast")
def forecast_api():
    location = request.args.get("city")
    return jsonify(get_forecast(location))

app.run(debug=True)
