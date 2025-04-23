from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("XO-MCP-Server")

@mcp.tool()
def k8s_deployment(
    registry_user: str, 
    registry_access_token: str, 
    image_name: str, 
    workspace_name: str, 
    app_name: str
    ) -> str:

    url = "http://3.109.184.200:5009/k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }
    data = {
        "registry_user": registry_user,
        "registry_access_token": registry_access_token,
        "image_name": image_name,
        "workspace_name": workspace_name,
        "app_name": app_name
    }

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
def start_k8s_deployment(
    workspace_name: str,
    app_name: str
) -> str:
    url = "http://3.109.184.200:5009/start-k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }
    data = {
        "workspace_name": workspace_name,
        "app_name": app_name
    }
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
def stop_k8s_deployment(
    workspace_name: str,
    app_name: str
) -> str:
    url = "http://3.109.184.200:5009/stop-k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }
    data = {
        "workspace_name": workspace_name,
        "app_name": app_name
    }
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
def remove_k8s_deployment(
    workspace_name: str,
    app_name: str
) -> str:
    url = "http://3.109.184.200:5009/remove-k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }
    data = {
        "workspace_name": workspace_name,
        "app_name": app_name
    }
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
def get_k8s_pod_logs(
    workspace_name: str,
    app_name: str
) -> str:
    url = "http://3.109.184.200:5009/get-k8s-pod-logs"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }
    data = {
        "workspace_name": workspace_name,
        "app_name": app_name
    }
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

