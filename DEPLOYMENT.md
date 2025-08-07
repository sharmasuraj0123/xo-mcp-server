# XO MCP Server Deployment Guide

This guide explains how to deploy your XO MCP Server so it can be used as a connector in ChatGPT.

## Prerequisites

- Python 3.11 or higher
- `uv` package manager
- `ACCESS_TOKEN` environment variable
- `DEPLOYMENT_ID` environment variable

## Local Deployment

### 1. Install Dependencies

```bash
uv sync
```

### 2. Set Environment Variables

```bash
export ACCESS_TOKEN=your_access_token_here
export DEPLOYMENT_ID=your_deployment_id_here
```

### 3. Run the Server

```bash
# Option 1: Using the deployment script
./deploy.sh

# Option 2: Direct Python execution
python3 -m xo_mcp_server.xo_mcp_server

# Option 3: Using uvx (for development)
uvx your_github_repo.git
```

The server will start on `http://0.0.0.0:5000` and expose an SSE endpoint at `/sse`.

## Cloud Deployment Options

### Option 1: Railway

1. Create a `railway.toml` file:
```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "python3 -m xo_mcp_server.xo_mcp_server"
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "on_failure"
```

2. Set environment variables in Railway dashboard:
   - `ACCESS_TOKEN`
   - `DEPLOYMENT_ID`

3. Deploy to Railway

### Option 2: Render

1. Create a `render.yaml` file:
```yaml
services:
  - type: web
    name: xo-mcp-server
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python3 -m xo_mcp_server.xo_mcp_server
    envVars:
      - key: ACCESS_TOKEN
        sync: false
      - key: DEPLOYMENT_ID
        sync: false
```

2. Deploy to Render

### Option 3: Heroku

1. Create a `Procfile`:
```
web: python3 -m xo_mcp_server.xo_mcp_server
```

2. Set environment variables in Heroku dashboard
3. Deploy to Heroku

### Option 4: DigitalOcean App Platform

1. Create a `app.yaml` file:
```yaml
name: xo-mcp-server
services:
  - name: web
    source_dir: /
    github:
      repo: your-username/your-repo
      branch: main
    run_command: python3 -m xo_mcp_server.xo_mcp_server
    environment_slug: python
    envs:
      - key: ACCESS_TOKEN
        scope: RUN_AND_BUILD_TIME
        value: ${ACCESS_TOKEN}
      - key: DEPLOYMENT_ID
        scope: RUN_AND_BUILD_TIME
        value: ${DEPLOYMENT_ID}
```

## ChatGPT Integration

Once your server is deployed, configure ChatGPT to use your MCP server:

1. Go to ChatGPT settings
2. Navigate to "Model Customization" or "Connectors"
3. Add your MCP server with this configuration:

```json
{
  "mcpServers": {
    "XO-MCP-Server": {
      "url": "https://your-deployed-domain.com/sse"
    }
  }
}
```

Replace `https://your-deployed-domain.com` with your actual deployed URL.

## Available Tools

Your MCP server provides these tools:

- `deploy_to_xo` - Deploy to XO
- `start_xo_app` - Start the XO app
- `stop_xo_app` - Stop the XO app
- `remove_xo_app` - Remove the XO app
- `get_xo_app_logs` - Get the XO app logs
- `expose_xo_app` - Expose the XO app to domain name

## Troubleshooting

### Server won't start
- Check if port 5000 is available
- Verify environment variables are set
- Check Python version (requires 3.11+)

### Connection issues
- Ensure the server is accessible from the internet
- Check firewall settings
- Verify the URL in ChatGPT configuration

### Tool execution errors
- Verify `ACCESS_TOKEN` and `DEPLOYMENT_ID` are correct
- Check network connectivity to XO backend
- Review server logs for detailed error messages 