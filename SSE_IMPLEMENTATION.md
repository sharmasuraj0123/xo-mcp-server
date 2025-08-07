# XO MCP Server SSE Implementation

This document describes the Server-Sent Events (SSE) implementation for the XO MCP Server.

## Overview

The XO MCP Server has been configured to work with Server-Sent Events (SSE) transport, which allows for real-time communication between MCP clients and the server. This implementation follows the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/overview) specification.

## Configuration

### MCP Client Configuration

The server is configured in your `~/.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "XO-MCP-Server": {
      "url": "https://003b37decbb4.ngrok-free.app/sse",
      "transport": "http"
    }
  }
}
```

### Key Configuration Points

- **URL**: Points to the SSE endpoint (`/sse`)
- **Transport**: Set to `"http"` for SSE transport
- **Endpoint**: The server exposes the `/sse` endpoint for MCP communication

## Implementation Details

### SSE Protocol Compliance

The implementation follows the SSE protocol specification:

1. **Content-Type**: `text/event-stream`
2. **Headers**: 
   - `Cache-Control: no-cache`
   - `Connection: keep-alive`
   - `Access-Control-Allow-Origin: *`
   - `Access-Control-Allow-Headers: *`

3. **Response Format**: Each response is formatted as `data: <json>\n\n`

### MCP Protocol Support

The server supports the following MCP methods:

1. **`initialize`**: Handles client initialization
2. **`tools/list`**: Returns available tools
3. **`tools/call`**: Executes specific tools

### Error Handling

The implementation includes proper error handling with JSON-RPC 2.0 error codes:

- `-32700`: Parse error
- `-32600`: Invalid Request
- `-32601`: Method not found
- `-32602`: Invalid params
- `-32603`: Internal error

## Available Tools

The server provides the following tools:

1. **`hello_connector`**: Simple test tool
2. **`deploy_to_xo`**: Deploy to XO platform
3. **`start_xo_app`**: Start XO application
4. **`stop_xo_app`**: Stop XO application
5. **`remove_xo_app`**: Remove XO application
6. **`get_xo_app_logs`**: Get application logs
7. **`expose_xo_app`**: Expose application to domain

## Testing

Use the provided test script to verify the SSE implementation:

```bash
python test_sse.py
```

The test script will:
1. Test basic SSE connection
2. Test MCP initialization
3. Test tools listing
4. Test tool execution

## Deployment

The server is configured to run on:
- **Host**: `0.0.0.0` (all interfaces)
- **Port**: `5000`
- **Framework**: FastAPI with Uvicorn

## Security Considerations

- CORS is enabled for all origins (configure as needed for production)
- Environment variables are used for sensitive data (ACCESS_TOKEN, DEPLOYMENT_ID)
- Proper error handling prevents information leakage

## Troubleshooting

### Common Issues

1. **Connection Refused**: Ensure the server is running and accessible
2. **CORS Errors**: Check CORS configuration in production
3. **Tool Execution Errors**: Verify environment variables are set correctly

### Logs

The server provides detailed logging for debugging:
- Request/response logging
- Error logging with stack traces
- Tool execution logging

## References

- [Model Context Protocol Overview](https://modelcontextprotocol.io/overview)
- [Server-Sent Events Specification](https://html.spec.whatwg.org/multipage/server-sent-events.html)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification) 