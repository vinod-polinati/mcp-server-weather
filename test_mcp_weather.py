import asyncio
from mcp.client.stdio import stdio_client
import json

async def test_mcp_weather():
    """Test the MCP weather server"""
    try:
        # Connect to the weather server
        async with stdio_client(["python3", "weather.py"]) as (read, write):
            # List available tools
            response = await write.call(
                "tools/list",
                {}
            )
            print("Available tools:", response)
            
            # Test the get_weather tool
            weather_response = await write.call(
                "tools/call",
                {
                    "name": "get_weather",
                    "arguments": {"location": "London"}
                }
            )
            print("\nWeather Response:")
            print(weather_response)
            
    except Exception as e:
        print(f"Error testing MCP weather: {e}")

if __name__ == "__main__":
    asyncio.run(test_mcp_weather()) 