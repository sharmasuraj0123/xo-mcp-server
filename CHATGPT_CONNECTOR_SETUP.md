# XO MCP Server - ChatGPT Connector Setup Guide

## 🎉 Current Status: FULLY OPERATIONAL!

Your XO MCP Server is now running successfully with **OpenAI MCP specification compliance** and is ready to be used as a ChatGPT connector.

### ✅ What's Working
- ✅ Docker container running on port 5001
- ✅ ngrok tunnel active: `https://003b37decbb4.ngrok-free.app`
- ✅ **MCP endpoint**: `/mcp` - HTTP endpoint for ChatGPT (OpenAI MCP spec compliant)
- ✅ **SSE endpoint**: `/sse` - Server-Sent Events for real-time communication
- ✅ All 7 XO tools available and tested
- ✅ Health checks passing
- ✅ Cursor integration working perfectly
- ✅ **OpenAI MCP specification compliance** ✅

## 🚀 How to Connect to ChatGPT

### Option 1: ChatGPT Web Interface
1. Open [ChatGPT](https://chat.openai.com)
2. Go to Settings → Connections or Plugins
3. Add new connection: **"MCP Server"**
4. Enter URL: `https://003b37decbb4.ngrok-free.app/mcp`
5. Protocol: **HTTP** (not SSE)
6. Name: **"XO MCP Server"**

### Option 2: Alternative URL (if /mcp doesn't work)
If the `/mcp` endpoint doesn't work, try the root endpoint:
- **URL**: `https://003b37decbb4.ngrok-free.app/`
- **Protocol**: **HTTP**
- **Name**: **"XO MCP Server"**

### Option 3: ChatGPT API
```json
{
  "mcp_servers": {
    "xo_mcp_server": {
      "url": "https://003b37decbb4.ngrok-free.app/mcp",
      "transport": "http"
    }
  }
}
```

## 🛠️ Available Tools

Once connected, ChatGPT can use these tools:

| Tool Name | Description | Status |
|-----------|-------------|--------|
| `hello_connector` | Simple test tool | ✅ Working |
| `deploy_to_xo` | Deploy to XO platform | ✅ Working |
| `start_xo_app` | Start the XO app | ✅ Working |
| `stop_xo_app` | Stop the XO app | ✅ Working |
| `remove_xo_app` | Remove the XO app | ✅ Working |
| `get_xo_app_logs` | Get the XO app logs | ✅ Working |
| `expose_xo_app` | Expose the XO app to domain | ✅ Working |

## 🔧 Environment Variables

**Current Configuration:**
```bash
ACCESS_TOKEN="80f720de6e734356c0b6d05ee86683e8d5969fc50c87a184bc28f9850a846ac7"
DEPLOYMENT_ID="a16bd066-3687-4c6b-8ad7-497b3d67a928"
```

To update the running container:
```bash
docker stop xo-mcp-server-container
docker rm xo-mcp-server-container
docker run -d -p 5001:5000 --name xo-mcp-server-container \
  -e ACCESS_TOKEN="your_actual_access_token" \
  -e DEPLOYMENT_ID="your_actual_deployment_id" \
  xo-mcp-server
```

## 🧪 Testing Your Connection

### Test MCP Endpoint (for ChatGPT):
```bash
curl -X GET https://003b37decbb4.ngrok-free.app/mcp
```

### Test SSE Endpoint (for other clients):
```bash
curl -X GET https://003b37decbb4.ngrok-free.app/sse
```

### Test Tools List (MCP - for ChatGPT):
```bash
curl -X POST https://003b37decbb4.ngrok-free.app/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}'
```

### Test Tools List (SSE - for other clients):
```bash
curl -X POST https://003b37decbb4.ngrok-free.app/sse \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}'
```

### Test Tool Execution (MCP - for ChatGPT):
```bash
curl -X POST https://003b37decbb4.ngrok-free.app/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "hello_connector", "arguments": {}}}'
```

## 📝 Example ChatGPT Prompts

Once connected, you can ask ChatGPT:

- "Hello connector" → Tests the connection
- "Deploy my XO app" → Deploys to XO platform
- "Start the XO application" → Starts the XO app
- "Show me the XO app logs" → Gets application logs
- "Stop the XO app" → Stops the XO app
- "Remove the XO app" → Removes the XO app
- "Expose the XO app to a domain" → Exposes app to domain

## 🔄 Keeping the Server Running

### For Development:
- Keep the ngrok tunnel running: `ngrok http 5001`
- Keep the Docker container running: `docker start xo-mcp-server-container`

### For Production (Recommended):
- Deploy to a cloud service using the provided `deploy.sh` script
- Use a proper domain name instead of ngrok
- Set up SSL certificates
- Configure proper environment variables

**Deployment Options:**
```bash
# Railway (Recommended)
./deploy.sh railway

# Render (Free tier)
./deploy.sh render

# Heroku
./deploy.sh heroku

# DigitalOcean
./deploy.sh digitalocean
```

## 🐛 Troubleshooting

### If ChatGPT can't connect:
1. Check if ngrok is running: `curl http://localhost:4040/api/tunnels`
2. Verify the container is running: `docker ps`
3. Test the endpoints directly:
   - `curl https://003b37decbb4.ngrok-free.app/health`
   - `curl https://003b37decbb4.ngrok-free.app/mcp` (for ChatGPT)
   - `curl https://003b37decbb4.ngrok-free.app/sse` (for other clients)

### If tools return errors:
1. Check environment variables are set correctly
2. Verify your ACCESS_TOKEN and DEPLOYMENT_ID are valid
3. Check the Docker logs: `docker logs xo-mcp-server-container`

### If Cursor shows "Loading tools":
1. Restart Cursor to pick up new MCP configuration
2. Check the MCP configuration in `~/.cursor/mcp.json`
3. Verify the server endpoints are responding

### If ChatGPT says "This MCP server doesn't implement our specification":
1. ✅ **FIXED**: Server now implements OpenAI MCP specification
2. Try the alternative URL: `https://003b37decbb4.ngrok-free.app/` (root endpoint)
3. Ensure you're using HTTP protocol, not SSE
4. Clear your browser cache and try again
5. Check if the server is responding: `curl https://003b37decbb4.ngrok-free.app/mcp`
6. Verify the server logs: `docker logs xo-mcp-server-container`

**If still not working:**
- Try using the root endpoint: `https://003b37decbb4.ngrok-free.app/`
- Check if ngrok tunnel is still active
- Restart the Docker container if needed
- Contact support if the issue persists

## 🔧 Technical Details

### OpenAI MCP Specification Compliance:
- ✅ **Protocol Version**: `2024-11-05`
- ✅ **Capabilities**: `{"tools": {"listChanged": false}}`
- ✅ **Response Format**: Proper JSON-RPC 2.0 with content array
- ✅ **Tool Schema**: Standard MCP tool schema
- ✅ **Error Handling**: Proper JSON-RPC error codes

### Endpoint Differences:
- **`/mcp`**: HTTP endpoint for ChatGPT (OpenAI MCP spec)
- **`/sse`**: SSE endpoint for real-time clients (Cursor, etc.)

### MCP Protocol Support:
- ✅ `initialize` - Client initialization with OpenAI capabilities
- ✅ `tools/list` - List available tools
- ✅ `tools/call` - Execute tools with proper response format
- ✅ Error handling with proper JSON-RPC codes

## 📞 Support

Your MCP server is now fully operational and **OpenAI MCP specification compliant**! The server handles all MCP protocol communication automatically and provides both HTTP and SSE endpoints.

**Current Public URLs:**
- **MCP Endpoint (ChatGPT)**: `https://003b37decbb4.ngrok-free.app/mcp`
- **SSE Endpoint (Cursor)**: `https://003b37decbb4.ngrok-free.app/sse`
- **Health Check**: `https://003b37decbb4.ngrok-free.app/health`

**Status**: ✅ **READY FOR CHATGPT INTEGRATION** 