from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("XO-MCP-Server")
backend_url = "https://devops-agent-api.xo.builders"
SWARM_URL = "https://dev-xo-swarm-api-xo-qk4zsdc.hello-xo.nl"

@mcp.tool()
def deploy_to_xo() -> str:
    '''
    Deploy to XO
    '''

    url = f"{backend_url}/deploy-to-xo"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

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
def start_xo_app() -> str:
    '''
    Start the XO app
    '''

    url = f"{backend_url}/start-xo-app"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {"DEPLOYMENT_ID": deployment_id}
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
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
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

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
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

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
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

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
def expose_xo_app() -> str:
    '''
    Expose the XO app to the domain name by calling the /expose-xo-app endpoint
    '''
    
    url = f"{backend_url}/expose-xo-app"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

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

