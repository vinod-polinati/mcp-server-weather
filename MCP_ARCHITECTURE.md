# MCP (Model Context Protocol) Project Architecture

## 🏗️ MCP Components

### 1. MCP Servers (Tools)
These are standalone services that provide specific functionality:

#### 🌤️ Weather Server (`weather.py`)
- **Transport**: `streamable-http` (runs on http://127.0.0.1:8000)
- **Tool**: `get_weather(location: str) -> str`
- **API**: Uses WeatherAPI.com for real weather data
- **Returns**: Temperature, conditions, humidity, wind speed

#### 🧮 Math Server (`mathserver.py`)
- **Transport**: `stdio` (command-line communication)
- **Tools**:
  - `add(a: int, b: int) -> int`
  - `subtract(a: int, b: int) -> int`
  - `multiply(a: int, b: int) -> int`

### 2. MCP Client (`client.py`)
- **Framework**: LangChain with MCP adapters
- **Model**: Groq LLM (llama-3.3-70b-versatile)
- **Agent**: ReAct agent that can use multiple MCP tools
- **Connects to**: Both weather and math servers

## 🔄 How It Works

```
User Query → LangChain Client → MCP Adapters → MCP Servers
                ↓
         Groq LLM (llama-3.3-70b-versatile)
                ↓
         ReAct Agent decides which tools to use
                ↓
         MCP Client calls appropriate servers:
         - Weather: HTTP transport
         - Math: stdio transport
                ↓
         Real API calls (WeatherAPI.com) or calculations
                ↓
         Results returned to user
```

## 🚀 Running the Project

### 1. Start MCP Servers
```bash
# Terminal 1: Start weather server
source .venv/bin/activate
python3 weather.py

# Terminal 2: Start math server (if needed)
source .venv/bin/activate
python3 mathserver.py
```

### 2. Run MCP Client
```bash
source .venv/bin/activate
python3 client.py
```

## 🎯 MCP Benefits

1. **Modularity**: Each server is independent and can be developed/deployed separately
2. **Language Agnostic**: MCP servers can be written in any language
3. **Scalability**: Easy to add new tools by creating new MCP servers
4. **Standardization**: Uses the MCP protocol for consistent communication
5. **Real-time Data**: Weather server provides live data from WeatherAPI.com

## 🔧 Environment Variables

```bash
# .env file
GROQ_API_KEY=your_groq_api_key
WEATHERAPI_KEY=your_weatherapi_key
```

This is a complete MCP implementation with real-world API integration! 🌟
