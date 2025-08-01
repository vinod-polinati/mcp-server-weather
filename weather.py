from mcp.server.fastmcp import FastMCP
import httpx
import os
from typing import Optional

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the current weather for a location.
    
    Args:
        location: City name, state, or country (e.g., "New York", "London", "Tokyo")
    
    Returns:
        Current weather information including temperature, conditions, and humidity
    """
    # Get API key from environment variable
    api_key = os.getenv("WEATHERAPI_KEY")
    if not api_key:
        return "Error: WEATHERAPI_KEY environment variable not set. Please set your WeatherAPI.com API key."
    
    try:
        # Make API request to WeatherAPI.com
        url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            "key": api_key,
            "q": location,
            "aqi": "no"  # No air quality data to keep it simple
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        
        # Extract weather information from WeatherAPI.com response
        location_info = data["location"]
        current = data["current"]
        
        temp_c = current["temp_c"]
        feels_like_c = current["feelslike_c"]
        humidity = current["humidity"]
        condition = current["condition"]["text"]
        wind_kph = current["wind_kph"]
        wind_mph = current["wind_mph"]
        
        # Format the response
        weather_info = f"Weather in {location_info['name']}, {location_info['country']}:\n"
        weather_info += f"• Temperature: {temp_c}°C (feels like {feels_like_c}°C)\n"
        weather_info += f"• Conditions: {condition}\n"
        weather_info += f"• Humidity: {humidity}%\n"
        weather_info += f"• Wind Speed: {wind_kph} km/h ({wind_mph} mph)"
        
        return weather_info
        
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 400:
            return f"Error: Location '{location}' not found. Please check the spelling and try again."
        else:
            return f"Error: HTTP {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")