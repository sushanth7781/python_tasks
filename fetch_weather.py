import requests

API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(city):
    params = {
        "latitude": 17.6868, 
        "longitude": 83.2185,
        "current_weather": True
    }
    
    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()
        
        data = response.json() 
        print(" Full API Response:", data) 
        weather = data.get("current_weather", {})
        print(f"\n Weather in {city}:")
        print(f"Temperature: {weather.get('temperature', 'N/A')}°C")
        print(f"Wind Speed: {weather.get('windspeed', 'N/A')} km/h")
        print(f"Condition: {weather.get('weathercode', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print(f"❌Error fetching weather data: {e}")


fetch_weather("Visakhapatnam")
