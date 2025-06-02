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
            ],
            "env": {
                "ACCESS_TOKEN": "your_access_token:contact_team_XO",
                "DEPLOYMENT_ID": "deployment_id_can_be_fount_at:https://launchpad.xo.builders/"
      }
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

### Working With XO MCP
Step 1: Goto our frontend, login to our app and create a project by giving it a project name:
```json
{
    "project_name": "newproj01"
}
```

Outcome:
You will get an robot_info.name and robot_info.secret and a DEPLOYMENT_ID

Step 2: Execute the below commands (commands can be shown in our frontend: https://launchpad.xo.builders/):

```
docker login registry.xo.builders -u 'username' -p your_password
```

- username is same as robot_info.name and it should be in quotes i.e 'xo-projname+imagename'
- password is same as robot_info.secret

```
docker image build -t registry.xo.builders/newproj01/newimgname .
```

====== OR ========

```
docker build --platform linux/amd64,linux/arm64 -t registry.xo.builders/newproj01/newimgname:latest .
```

```
docker image push registry.xo.builders/projname/newimgname
```

Step 3: Open the cursor settings and goto MCP and add our MCP Server:
- more details above

Step 4: In our MCP env, provide DEPLOYMENT_ID you got on Step 1:

- MCP Should look something like:
```json
{
    "mcpServers": {
        "XO-MCP-Server": {
            "command": "uvx",
            "args": [
                "git+https://github.com/sharmasuraj0123/xo-mcp-server.git"
            ],
            "env": {
                "ACCESS_TOKEN": "your_access_token:contact_team_XO",
                "DEPLOYMENT_ID": "deployment_id_can_be_fount_at:https://launchpad.xo.builders/"
      }
        }
    }
}
```

Step 5: Hurray! 🎉 You have successfully completed the XO-MCP setup.

- Type this to cursor chat: Deploy to XO
- Outcome: You have Successfully deloyed to XO.

Step 6:You can now perform other optional operations:
- Stop XO app
- Remove XO app
- Start XO app
- Get XO app logs

Step 7: Type this to chat: Expose XO app:

