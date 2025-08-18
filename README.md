# XO MCP Server

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-1.6.0+-green.svg)](https://github.com/modelcontextprotocol/python-sdk)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A powerful Model Context Protocol (MCP) server that provides seamless integration with the XO platform for container deployment, application lifecycle management, and knowledge base operations. This server enables AI assistants to deploy, manage, and interact with applications on the XO infrastructure through natural language commands.

## 🚀 Features

### Container Deployment & Management
- **One-click deployment** to XO platform
- **Lifecycle management** (start, stop, remove applications)
- **Real-time logging** and monitoring
- **Application exposure** with automatic domain provisioning

### Knowledge Base Integration
- **Dynamic knowledge base updates** using text content
- **Intelligent question answering** with context-aware responses
- **Multi-project support** with isolated knowledge bases
- **Flexible agent types** for different use cases

### Developer Experience
- **Simple setup** with environment-based configuration
- **Comprehensive error handling** with detailed feedback
- **Modern MCP architecture** using FastMCP
- **Cross-platform compatibility**

## 📋 Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- XO platform account with valid credentials
- MCP-compatible client (Claude Desktop, Cursor, etc.)

## 🛠️ Installation

### Option 1: Direct from GitHub (Recommended)

Add this configuration to your MCP client settings:

```json
{
  "mcpServers": {
    "xo-mcp-server": {
      "command": "uvx",
      "args": [
        "git+https://github.com/sharmasuraj0123/xo-mcp-server.git"
      ],
      "env": {
        "ACCESS_TOKEN": "your_access_token",
        "DEPLOYMENT_ID": "your_deployment_id"
      }
    }
  }
}
```

### Option 2: Local Development

1. Clone the repository:
```bash
git clone https://github.com/sharmasuraj0123/xo-mcp-server.git
cd xo-mcp-server
```

2. Add to your MCP client settings:
```json
{
  "mcpServers": {
    "xo-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/xo-mcp-server",
        "run",
        "-m",
        "xo_mcp_server"
      ],
      "env": {
        "ACCESS_TOKEN": "your_access_token",
        "DEPLOYMENT_ID": "your_deployment_id"
      }
    }
  }
}
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ACCESS_TOKEN` | Your XO platform access token | ✅ |
| `DEPLOYMENT_ID` | Unique deployment identifier from XO Launchpad | ✅ |

### Getting Your Credentials

1. Visit [XO Launchpad](https://launchpad.xo.builders/)
2. Login and create a new project
3. Note down your `DEPLOYMENT_ID`
4. Contact the XO team for your `ACCESS_TOKEN`

## 🔧 Available Tools

### Container Management

#### `deploy_to_xo()`
Deploy your containerized application to the XO platform.

**Usage:** "Deploy my application to XO"

#### `start_xo_app()`
Start a previously deployed application.

**Usage:** "Start my XO application"

#### `stop_xo_app()`
Stop a running application without removing it.

**Usage:** "Stop my XO application"

#### `remove_xo_app()`
Completely remove an application from the platform.

**Usage:** "Remove my XO application"

#### `get_xo_app_logs()`
Retrieve real-time logs from your running application.

**Usage:** "Show me the logs for my XO app"

#### `expose_xo_app()`
Expose your application to the internet with a custom domain.

**Usage:** "Expose my XO app to the internet"

### Knowledge Base Operations

#### `update_knowledgebase_using_text(project_name, text_content, text_id?)`
Add or update text content in your project's knowledge base.

**Parameters:**
- `project_name` (string): Name of your XO project
- `text_content` (string): The text content to add/update
- `text_id` (string, optional): Unique identifier for the text content

**Usage:** "Update my knowledge base with this documentation"

#### `ask_question(project_name, question, user_id?, agent_type?, message_type?)`
Query your project's knowledge base with intelligent responses.

**Parameters:**
- `project_name` (string): Name of your XO project
- `question` (string): Your question
- `user_id` (string, optional): User identifier (default: "default_user")
- `agent_type` (string, optional): Type of agent response (default: "normal")
- `message_type` (string, optional): Message type (default: "@xo")

**Usage:** "Ask my knowledge base about deployment procedures"

## 🚀 Quick Start Guide

### 1. Set Up Your XO Project

1. Go to [XO Launchpad](https://launchpad.xo.builders/)
2. Login and create a new project:
   ```json
   {
     "project_name": "my-awesome-app"
   }
   ```
3. Save your `DEPLOYMENT_ID` and obtain your `ACCESS_TOKEN`

### 2. Prepare Your Container

Build and push your Docker image to the XO registry:

```bash
# Login to XO registry
docker login registry.xo.builders -u 'your-robot-name' -p 'your-robot-secret'

# Build your image
docker build --platform linux/amd64,linux/arm64 -t registry.xo.builders/your-project/your-app:latest .

# Push to registry
docker push registry.xo.builders/your-project/your-app:latest
```

### 3. Configure MCP Client

Add the server configuration to your MCP client (Claude Desktop, Cursor, etc.) with your credentials.

### 4. Deploy and Manage

Once configured, you can use natural language commands:

- "Deploy my application to XO"
- "Show me the application logs"
- "Expose my app to the internet"
- "Update my knowledge base with the latest documentation"

## 🏗️ Architecture

The XO MCP Server is built on the FastMCP framework and provides:

- **RESTful API integration** with XO backend services
- **Robust error handling** with detailed error messages
- **Environment-based configuration** for security
- **Modular tool architecture** for easy extension

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation:** [XO Launchpad](https://launchpad.xo.builders/)
- **Issues:** [GitHub Issues](https://github.com/sharmasuraj0123/xo-mcp-server/issues)
- **Contact:** Contact the XO team for access tokens and support

## 🔗 Related Projects

- [Model Context Protocol](https://github.com/modelcontextprotocol)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [XO Platform](https://xo.builders/)

---

Built with ❤️ by the XO team
