# XO MCP Server

A Model Context Protocol (MCP) server for XO app management.

## Features

- Deploy to XO
- Start XO app
- Stop XO app
- Remove XO app
- Get XO app logs
- Expose XO app to domain name

## Installation

```bash
uv sync
```

## Usage

```bash
export ACCESS_TOKEN=your_token_here
export DEPLOYMENT_ID=your_deployment_id_here
python3 -m xo_mcp_server
```

## Docker

```bash
docker build -t xo-mcp-server .
docker run -p 5000:5000 -e ACCESS_TOKEN -e DEPLOYMENT_ID xo-mcp-server
```

```

