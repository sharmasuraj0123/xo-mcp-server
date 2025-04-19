from mcp.server.fastmcp import FastMCP
import requests

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
        "Access-Token": "80f720de6e734356c0b6d05ee86683e8d5969fc50c87a184bc28f9850a846ac7"
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

