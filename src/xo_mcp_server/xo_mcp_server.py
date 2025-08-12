from mcp.server.fastmcp import FastMCP
import requests
import os
from typing import Optional
from contextvars import ContextVar
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request as FastAPIRequest
from starlette.middleware import Middleware

mcp = FastMCP("XO-MCP-Server")
# backend_url = "https://api-launchpad-v1.xo.builders/"
backend_url = "https://devops-agent-api.xo.builders"
SWARM_URL = "https://dev-xo-swarm-api-xo-qk4zsdc.hello-xo.nl"

# Context variable to store request headers
request_headers: ContextVar[Optional[dict]] = ContextVar('request_headers', default=None)

class HeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Store headers in context
        headers_dict = dict(request.headers)
        request_headers.set(headers_dict)
        response = await call_next(request)
        return response

# Create a custom FastAPI app with middleware
app = FastAPI(middleware=[Middleware(HeaderMiddleware)])

# Override the FastMCP app with our custom app
mcp._app = app

def get_header_value(header_name: str) -> Optional[str]:
    """Get header value from request context or environment variables"""
    headers = request_headers.get()
    if headers and header_name in headers:
        return headers[header_name]
    return os.getenv(header_name)

def get_auth_token() -> Optional[str]:
    """Get access token from headers or environment"""
    return get_header_value("Authorization") or get_header_value("ACCESS_TOKEN")

def get_deployment_id() -> Optional[str]:
    """Get deployment ID from headers or environment"""
    return get_header_value("DEPLOYMENT_ID")

@mcp.tool()
def hello_connector() -> str:
    '''
    A simple test tool that says Hello Connector!
    '''
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    return f"Hello Connector! Your MCP server is working perfectly! 🎉 Auth: {auth_token}, Deployment: {deployment_id}"

@mcp.tool()
def deploy_to_xo() -> str:
    '''
    Deploy to XO
    '''

    url = f"{backend_url}/deploy-to-xo"
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    
    if not auth_token:
        return "ACCESS_TOKEN not found in headers or environment"
    
    if not deployment_id:
        return "DEPLOYMENT_ID not found in headers or environment"

    # Clean up auth token (remove "Bearer " prefix if present)
    if auth_token.startswith("Bearer "):
        auth_token = auth_token[7:]

    headers = {
        "Content-Type": "application/json",
        "Access-Token": auth_token
    }

    data = {"DEPLOYMENT_ID": deployment_id}

    try:
        response = requests.post(url, headers=headers, json=data)
        return f"Response: {response.text} and data: {data}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)

@mcp.tool()
def start_xo_app() -> str:
    '''
    Start the XO app
    '''

    url = f"{backend_url}/start-xo-app"
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    
    if not auth_token:
        return "ACCESS_TOKEN not found in headers or environment"
    
    if not deployment_id:
        return "DEPLOYMENT_ID not found in headers or environment"

    # Clean up auth token (remove "Bearer " prefix if present)
    if auth_token.startswith("Bearer "):
        auth_token = auth_token[7:]

    headers = {
        "Content-Type": "application/json",
        "Access-Token": auth_token
    }

    data = {"DEPLOYMENT_ID": deployment_id}
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)     

@mcp.tool()
def stop_xo_app() -> str:
    '''
    Stop the XO app
    '''

    url = f"{backend_url}/stop-xo-app"
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    
    if not auth_token:
        return "ACCESS_TOKEN not found in headers or environment"
    
    if not deployment_id:
        return "DEPLOYMENT_ID not found in headers or environment"

    # Clean up auth token (remove "Bearer " prefix if present)
    if auth_token.startswith("Bearer "):
        auth_token = auth_token[7:]

    headers = {
        "Content-Type": "application/json",
        "Access-Token": auth_token
    }

    data = {"DEPLOYMENT_ID": deployment_id}
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)
    
@mcp.tool()
def remove_xo_app() -> str:
    '''
    Remove the XO app
    '''

    url = f"{backend_url}/remove-xo-app"
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    
    if not auth_token:
        return "ACCESS_TOKEN not found in headers or environment"
    
    if not deployment_id:
        return "DEPLOYMENT_ID not found in headers or environment"

    # Clean up auth token (remove "Bearer " prefix if present)
    if auth_token.startswith("Bearer "):
        auth_token = auth_token[7:]

    headers = {
        "Content-Type": "application/json",
        "Access-Token": auth_token
    }

    data = {"DEPLOYMENT_ID": deployment_id}
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)   
    
@mcp.tool()
def get_xo_app_logs() -> str:
    '''
    Get the XO app logs
    '''

    url = f"{backend_url}/get-xo-app-logs"
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    
    if not auth_token:
        return "ACCESS_TOKEN not found in headers or environment"
    
    if not deployment_id:
        return "DEPLOYMENT_ID not found in headers or environment"

    # Clean up auth token (remove "Bearer " prefix if present)
    if auth_token.startswith("Bearer "):
        auth_token = auth_token[7:]

    headers = {
        "Content-Type": "application/json",
        "Access-Token": auth_token
    }

    data = {"DEPLOYMENT_ID": deployment_id}
    try:
        response = requests.post(url, headers=headers, json=data)
        return f"Response: {response.text} and data: {data}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)

@mcp.tool()
def expose_xo_app() -> str:
    '''
    Expose the XO app to the domain name by calling the /expose-xo-app endpoint
    '''
    
    url = f"{backend_url}/expose-xo-app"
    auth_token = get_auth_token()
    deployment_id = get_deployment_id()
    
    if not auth_token:
        return "ACCESS_TOKEN not found in headers or environment"
    
    if not deployment_id:
        return "DEPLOYMENT_ID not found in headers or environment"

    # Clean up auth token (remove "Bearer " prefix if present)
    if auth_token.startswith("Bearer "):
        auth_token = auth_token[7:]

    headers = {
        "Content-Type": "application/json",
        "Access-Token": auth_token
    }

    data = {"DEPLOYMENT_ID": deployment_id}

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)

@mcp.tool()
def update_knowledgebase_using_text(project_name: str, text_content: str, text_id: str = None) -> str:
    '''
    Update knowledgebase using text content
    '''
    
    url = f"{SWARM_URL}/update-knowledgebase-using-text"
    
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "project_name": project_name,
        "text": text_content
    }
    
    # Add text_id if provided
    if text_id:
        data["text_id"] = text_id

    try:
        response = requests.post(url, headers=headers, json=data)
        return f"Response: {response.text} and data: {data}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)

@mcp.tool()
def ask_question(project_name: str, question: str, user_id: str = "default_user", agent_type: str = "normal", message_type: str = "@xo") -> str:
    '''
    Ask a question to the knowledge base
    '''
    
    url = f"{SWARM_URL}/ask_question"
    
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "project_name": project_name,
        "user_id": user_id,
        "question": question,
        "type": agent_type,
        "message_type": message_type
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return f"Response: {response.text} and data: {data}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"
    except Exception as e:
        return str(e)

# Server configuration for deployment
if __name__ == "__main__":
    # Run the MCP server on a specific host and port for deployment
    mcp.run(host="0.0.0.0", port=5001)
    