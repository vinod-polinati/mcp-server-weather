import asyncio
import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

async def test_weather_api():
    """Test the WeatherAPI.com API directly"""
    api_key = os.getenv("WEATHERAPI_KEY")
    if not api_key:
        print("❌ WEATHERAPI_KEY not set!")
        print("Please get a free API key from: https://www.weatherapi.com/")
        print("Then set it with: export WEATHERAPI_KEY=your_key_here")
        return
    
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": api_key,
            "q": "New York",
            "aqi": "no"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        
        print("✅ Weather API test successful!")
        location = data['location']
        current = data['current']
        print(f"Location: {location['name']}, {location['country']}")
        print(f"Temperature: {current['temp_c']}°C (feels like {current['feelslike_c']}°C)")
        print(f"Conditions: {current['condition']['text']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['wind_kph']} km/h")
        
    except Exception as e:
        print(f"❌ Weather API test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_weather_api()) 