#!/bin/bash

# XO MCP Server Deployment Script

echo "🚀 Deploying XO MCP Server..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install uv first."
    echo "Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
uv sync

# Set environment variables (you'll need to set these)
if [ -z "$ACCESS_TOKEN" ]; then
    echo "⚠️  ACCESS_TOKEN environment variable is not set"
    echo "Please set it with: export ACCESS_TOKEN=your_token_here"
fi

if [ -z "$DEPLOYMENT_ID" ]; then
    echo "⚠️  DEPLOYMENT_ID environment variable is not set"
    echo "Please set it with: export DEPLOYMENT_ID=your_deployment_id_here"
fi

# Run the server
echo "🌐 Starting XO MCP Server on http://0.0.0.0:5000"
echo "📋 For ChatGPT integration, use this configuration:"
echo "   URL: http://your-server-ip:5000/sse"
echo ""
echo "Press Ctrl+C to stop the server"

# Run the server
python3 -m xo_mcp_server 