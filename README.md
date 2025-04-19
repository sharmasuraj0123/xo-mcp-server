# XO MCP Server

A Python-based server implementation for XO MCP (Management Control Protocol) services.

## Table of Contents
- [Installation](#installation)
- [Local Development](#local-development)
- [GitHub Integration](#github-integration)
- [Configuration](#configuration)

## Installation

This project uses `uv` for Python package management. Make sure you have it installed before proceeding.

## Local Development

To run the server locally, add the following configuration to your MCP server settings:

```json
{
    "mcpServers": {
        "XO-MCP-Server": {
            "command": "uv",
            "args": [
                "--directory",
                "D:/Work/XO/MCP-Servers/xo-mcp-server",
                "run",
                "-m",
                "xo_mcp_server"
            ]
        }
    }
}
```

## GitHub Integration

To run the server directly from GitHub, use the following configuration:

```json
{
    "mcpServers": {
        "XO-MCP-Server": {
            "command": "uvx",
            "args": [
                "git+https://github.com/sharmasuraj0123/xo-mcp-server.git"
            ]
        }
    }
}
```

## Configuration

The server supports various configuration options through the MCP server settings. Make sure to update the paths and commands according to your local environment.

### Environment Variables
- Ensure all required environment variables are set before running the server
- Check the configuration files for any additional setup requirements

### Dependencies
- Python 3.x
- uv package manager
- Additional dependencies as specified in pyproject.toml