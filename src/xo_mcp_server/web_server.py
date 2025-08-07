from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
import logging
from typing import AsyncGenerator
import uvicorn
from .xo_mcp_server import mcp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="XO MCP Server", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "XO MCP Server is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "server": "XO MCP Server"}

@app.options("/mcp")
async def mcp_options():
    """
    Handle OPTIONS requests for CORS preflight
    """
    return {"message": "CORS preflight successful"}

@app.get("/mcp")
async def mcp_get():
    """
    GET endpoint for MCP health check
    """
    return {"message": "MCP endpoint is available", "method": "GET"}

@app.post("/")
async def root_mcp_endpoint(request: Request):
    """
    Root MCP endpoint that some clients might expect
    """
    return await mcp_endpoint(request)

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    """
    Standard MCP endpoint that handles MCP protocol communication
    """
    try:
        # Read the request body
        body = await request.body()
        
        # Check if body is empty
        if not body:
            return {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "Empty request body"}
            }
        
        try:
            data = json.loads(body)
        except json.JSONDecodeError as e:
            return {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
            }
        
        logger.info(f"Received MCP request: {data}")
        
        # Validate JSON-RPC format
        if "jsonrpc" not in data or data["jsonrpc"] != "2.0":
            return {
                "jsonrpc": "2.0",
                "id": data.get("id", 0),
                "error": {"code": -32600, "message": "Invalid Request: jsonrpc must be '2.0'"}
            }
        
        # Validate that method is present
        if "method" not in data:
            return {
                "jsonrpc": "2.0",
                "id": data.get("id", 0),
                "error": {"code": -32600, "message": "Invalid Request: method is required"}
            }
        
        # Handle different types of MCP requests
        method = data["method"]
        params = data.get("params", {})
        
        if method == "tools/list":
            # Return list of available tools with proper OpenAI MCP schema
            tools = []
            try:
                tool_list = await mcp.list_tools()
                for tool in tool_list:
                    # Create proper tool schema for OpenAI MCP
                    tool_schema = {
                        "name": tool.name,
                        "description": (tool.description or "").strip().replace('\n', ' ').replace('    ', ' '),
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                    tools.append(tool_schema)
                
                response = {
                    "jsonrpc": "2.0",
                    "id": data.get("id", 0),
                    "result": {"tools": tools}
                }
                logger.info(f"Sending tools list response: {response}")
                return response
            except Exception as e:
                logger.error(f"Error listing tools: {e}")
                return {
                    "jsonrpc": "2.0",
                    "id": data.get("id", 0),
                    "error": {"code": -32603, "message": f"Internal error: {str(e)}"}
                }
        
        elif method == "tools/call":
            # Execute a tool
            tool_name = params.get("name")
            tool_params = params.get("arguments", {})
            
            if not tool_name:
                return {
                    "jsonrpc": "2.0",
                    "id": data.get("id", 0),
                    "error": {"code": -32602, "message": "Invalid params: tool name is required"}
                }
            
            try:
                # Execute the tool using call_tool method
                result = await mcp.call_tool(tool_name, tool_params)
                
                # Format result according to OpenAI MCP spec
                content = []
                if isinstance(result, tuple):
                    # Handle FastMCP result format
                    text_content, metadata = result
                    if hasattr(text_content, '__iter__') and not isinstance(text_content, str):
                        # Handle list of TextContent objects
                        for item in text_content:
                            if hasattr(item, 'text'):
                                content.append({"type": "text", "text": item.text})
                            else:
                                content.append({"type": "text", "text": str(item)})
                    elif hasattr(text_content, 'text'):
                        content.append({"type": "text", "text": text_content.text})
                    else:
                        content.append({"type": "text", "text": str(text_content)})
                else:
                    content.append({"type": "text", "text": str(result)})
                
                response = {
                    "jsonrpc": "2.0",
                    "id": data.get("id", 0),
                    "result": {"content": content}
                }
                logger.info(f"Sending tool call response: {response}")
                return response
            except Exception as e:
                logger.error(f"Error executing tool {tool_name}: {e}")
                return {
                    "jsonrpc": "2.0",
                    "id": data.get("id", 0),
                    "error": {"code": -32603, "message": str(e)}
                }
        
        elif method == "initialize":
            # Handle initialization with OpenAI MCP capabilities
            # Extract client capabilities from params
            client_capabilities = params.get("capabilities", {})
            client_info = params.get("clientInfo", {})
            
            logger.info(f"Client capabilities: {client_capabilities}")
            logger.info(f"Client info: {client_info}")
            
            response = {
                "jsonrpc": "2.0",
                "id": data.get("id", 0),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {
                            "listChanged": False
                        }
                    },
                    "serverInfo": {
                        "name": "XO MCP Server",
                        "version": "1.0.0"
                    }
                }
            }
            logger.info(f"Sending initialize response: {response}")
            return response
        
        # Default response for unrecognized requests
        return {
            "jsonrpc": "2.0",
            "id": data.get("id", 0),
            "error": {"code": -32601, "message": f"Method not found: {method}"}
        }
        
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return {
            "jsonrpc": "2.0",
            "id": data.get("id", 0) if "data" in locals() else 0,
            "error": {"code": -32603, "message": str(e)}
        }

@app.get("/sse")
async def sse_get():
    """
    GET endpoint for SSE health check
    """
    return {"message": "SSE endpoint is available", "method": "GET"}

@app.post("/sse")
async def sse_endpoint(request: Request):
    """
    SSE endpoint that handles MCP protocol communication
    """
    try:
        # Read the request body
        body = await request.body()
        data = json.loads(body) if body else {}
        
        logger.info(f"Received SSE request: {data}")
        
        # Validate JSON-RPC format
        if "jsonrpc" not in data or data["jsonrpc"] != "2.0":
            return StreamingResponse(
                generate_sse_response({
                    "jsonrpc": "2.0",
                    "id": data.get("id", 0),
                    "error": {"code": -32600, "message": "Invalid Request"}
                }),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "*"
                }
            )
        
        # Handle different types of MCP requests
        if "method" in data:
            method = data["method"]
            params = data.get("params", {})
            
            if method == "tools/list":
                # Return list of available tools with proper OpenAI MCP schema
                tools = []
                try:
                    tool_list = await mcp.list_tools()
                    for tool in tool_list:
                        # Create proper tool schema for OpenAI MCP
                        tool_schema = {
                            "name": tool.name,
                            "description": (tool.description or "").strip().replace('\n', ' ').replace('    ', ' '),
                            "inputSchema": {
                                "type": "object",
                                "properties": {},
                                "required": []
                            }
                        }
                        tools.append(tool_schema)
                    
                    return StreamingResponse(
                        generate_sse_response({
                            "jsonrpc": "2.0",
                            "id": data.get("id", 0),
                            "result": {"tools": tools}
                        }),
                        media_type="text/event-stream",
                        headers={
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "*"
                        }
                    )
                except Exception as e:
                    logger.error(f"Error listing tools: {e}")
                    return StreamingResponse(
                        generate_sse_response({
                            "jsonrpc": "2.0",
                            "id": data.get("id", 0),
                            "error": {"code": -32603, "message": f"Internal error: {str(e)}"}
                        }),
                        media_type="text/event-stream",
                        headers={
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "*"
                        }
                    )
            
            elif method == "tools/call":
                # Execute a tool
                tool_name = params.get("name")
                tool_params = params.get("arguments", {})
                
                if not tool_name:
                    return StreamingResponse(
                        generate_sse_response({
                            "jsonrpc": "2.0",
                            "id": data.get("id", 0),
                            "error": {"code": -32602, "message": "Invalid params: tool name is required"}
                        }),
                        media_type="text/event-stream",
                        headers={
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "*"
                        }
                    )
                
                try:
                    # Execute the tool using call_tool method
                    result = await mcp.call_tool(tool_name, tool_params)
                    
                    # Format result according to OpenAI MCP spec
                    content = []
                    if isinstance(result, tuple):
                        # Handle FastMCP result format
                        text_content, metadata = result
                        if hasattr(text_content, '__iter__') and not isinstance(text_content, str):
                            # Handle list of TextContent objects
                            for item in text_content:
                                if hasattr(item, 'text'):
                                    content.append({"type": "text", "text": item.text})
                                else:
                                    content.append({"type": "text", "text": str(item)})
                        elif hasattr(text_content, 'text'):
                            content.append({"type": "text", "text": text_content.text})
                        else:
                            content.append({"type": "text", "text": str(text_content)})
                    else:
                        content.append({"type": "text", "text": str(result)})
                    
                    return StreamingResponse(
                        generate_sse_response({
                            "jsonrpc": "2.0",
                            "id": data.get("id", 0),
                            "result": {"content": content}
                        }),
                        media_type="text/event-stream",
                        headers={
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "*"
                        }
                    )
                except Exception as e:
                    logger.error(f"Error executing tool {tool_name}: {e}")
                    return StreamingResponse(
                        generate_sse_response({
                            "jsonrpc": "2.0",
                            "id": data.get("id", 0),
                            "error": {"code": -32603, "message": str(e)}
                        }),
                        media_type="text/event-stream",
                        headers={
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "*"
                        }
                    )
            
            elif method == "initialize":
                # Handle initialization with OpenAI MCP capabilities
                # Extract client capabilities from params
                client_capabilities = params.get("capabilities", {})
                client_info = params.get("clientInfo", {})
                
                logger.info(f"Client capabilities: {client_capabilities}")
                logger.info(f"Client info: {client_info}")
                
                return StreamingResponse(
                    generate_sse_response({
                        "jsonrpc": "2.0",
                        "id": data.get("id", 0),
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {
                                "tools": {
                                    "listChanged": False
                                }
                            },
                            "serverInfo": {
                                "name": "XO MCP Server",
                                "version": "1.0.0"
                            }
                        }
                    }),
                    media_type="text/event-stream",
                    headers={
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "*"
                    }
                )
        
        # Default response for unrecognized requests
        return StreamingResponse(
            generate_sse_response({
                "jsonrpc": "2.0",
                "id": data.get("id", 0),
                "error": {"code": -32601, "message": "Method not found"}
            }),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            }
        )
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return StreamingResponse(
            generate_sse_response({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "Parse error"}
            }),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            }
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return StreamingResponse(
            generate_sse_response({
                "jsonrpc": "2.0",
                "id": data.get("id", 0) if "data" in locals() else 0,
                "error": {"code": -32603, "message": str(e)}
            }),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            }
        )

async def generate_sse_response(data: dict) -> AsyncGenerator[str, None]:
    """
    Generate proper SSE response format
    """
    response_data = json.dumps(data)
    yield f"data: {response_data}\n\n"

def run_server(host: str = "127.0.0.1", port: int = 5001):
    """
    Run the web server
    """
    logger.info(f"Starting XO MCP Server on {host}:{port}")
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    run_server() 