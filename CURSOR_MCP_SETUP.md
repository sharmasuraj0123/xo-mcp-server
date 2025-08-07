# XO MCP Server - Cursor Setup Guide

## 🎉 MCP Server Fixed and Ready!

Your XO MCP Server has been updated to properly handle JSON-RPC format and should now work with both ChatGPT and Cursor.

## 🚀 How to Use with Cursor

### Step 1: Copy the MCP Configuration

Copy the `cursor-mcp.json` file to your Cursor configuration directory:

**On macOS:**
```bash
cp cursor-mcp.json ~/.cursor/mcp.json
```

**On Windows:**
```bash
copy cursor-mcp.json %APPDATA%\Cursor\mcp.json
```

**On Linux:**
```bash
cp cursor-mcp.json ~/.config/Cursor/mcp.json
```

### Step 2: Restart Cursor

After copying the configuration file, restart Cursor for the changes to take effect.

### Step 3: Test the MCP Server

In Cursor, you can now use the XO MCP tools:

- **Deploy to XO**: `deploy_to_xo`
- **Start XO App**: `start_xo_app`
- **Stop XO App**: `stop_xo_app`
- **Remove XO App**: `remove_xo_app`
- **Get XO App Logs**: `get_xo_app_logs`
- **Expose XO App**: `expose_xo_app`

## 🔧 Environment Variables

To make the tools work properly, you need to set environment variables in your Docker container:

```bash
docker stop xo-mcp-server-container
docker rm xo-mcp-server-container
docker run -d -p 5001:5000 --name xo-mcp-server-container \
  -e ACCESS_TOKEN="your_actual_access_token" \
  -e DEPLOYMENT_ID="your_actual_deployment_id" \
  xo-mcp-server
```

## 🧪 Testing Commands

### Test MCP Initialization:
```bash
curl -X POST https://fb10e4a81cad.ngrok-free.app/sse \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "initialize", "id": 1, "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0.0"}}}'
```

### Test Tools List:
```bash
curl -X POST https://fb10e4a81cad.ngrok-free.app/sse \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "tools/list", "id": 2, "params": {}}'
```

### Test Tool Execution:
```bash
curl -X POST https://fb10e4a81cad.ngrok-free.app/sse \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "tools/call", "id": 3, "params": {"name": "deploy_to_xo", "arguments": {}}}'
```

## 📝 Example Cursor Usage

Once configured, you can ask Cursor:

- "Deploy my XO app using the MCP server"
- "Start the XO application"
- "Show me the XO app logs"
- "Stop the XO app"
- "Remove the XO app"
- "Expose the XO app to a domain"

## 🔄 Keeping the Server Running

### For Development:
- Keep the ngrok tunnel running: `ngrok http 5001`
- Keep the Docker container running: `docker start xo-mcp-server-container`

### For Production:
- Deploy to a cloud service (AWS, GCP, Azure)
- Use a proper domain name
- Set up SSL certificates
- Configure proper environment variables

## 🐛 Troubleshooting

### If Cursor can't connect:
1. Check if ngrok is running: `curl http://localhost:4040/api/tunnels`
2. Verify the container is running: `docker ps`
3. Test the endpoint directly: `curl https://fb10e4a81cad.ngrok-free.app/health`

### If tools return errors:
1. Check environment variables are set correctly
2. Verify your ACCESS_TOKEN and DEPLOYMENT_ID are valid
3. Check the Docker logs: `docker logs xo-mcp-server-container`

## 📞 Support

Your MCP server is now ready to be used with Cursor! The server handles all the MCP protocol communication automatically.

**Current Public URL**: `https://fb10e4a81cad.ngrok-free.app/sse` 