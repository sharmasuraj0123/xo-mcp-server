from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("XO-MCP-Server")
backend_url = "https://devops-agent-api.xo.builders"

@mcp.tool()
def xo_k8s_deployment(
    # registry_user: str, 
    # registry_access_token: str, 
    # image_name: str, 
    # workspace_name: str, 
    # app_name: str
    ) -> str:

    url = f"{backend_url}/k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {
        # "registry_user": registry_user,
        # "registry_access_token": registry_access_token,
        # "image_name": image_name,
        # "workspace_name": workspace_name,
        # "app_name": app_name
        "DEPLOYMENT_ID": deployment_id
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
def xo_start_k8s_deployment(
    # workspace_name: str,
    # app_name: str
) -> str:
    url = f"{backend_url}/start-k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {
        # "workspace_name": workspace_name,
        # "app_name": app_name
        "DEPLOYMENT_ID": deployment_id
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
def xo_stop_k8s_deployment(
    # workspace_name: str,
    # app_name: str
) -> str:
    url = f"{backend_url}/stop-k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {
        # "workspace_name": workspace_name,
        # "app_name": app_name
        "DEPLOYMENT_ID": deployment_id
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
def xo_remove_k8s_deployment(
    # workspace_name: str,
    # app_name: str
) -> str:
    url = f"{backend_url}/remove-k8s-deployment"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {
        # "workspace_name": workspace_name,
        # "app_name": app_name
        "DEPLOYMENT_ID": deployment_id
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
def xo_get_k8s_pod_logs(
    # workspace_name: str,
    # app_name: str
) -> str:
    url = f"{backend_url}/get-k8s-pod-logs"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {
        # "workspace_name": workspace_name,
        # "app_name": app_name
        "DEPLOYMENT_ID": deployment_id
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
def xo_get_docker_containers() -> str:
    """
    Run docker ps command and return the list of running containers
    """
    try:
        # Using subprocess to run the shell command
        import subprocess
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error running docker ps: {result.stderr}"
    except FileNotFoundError:
        return "Docker command not found. Please ensure Docker is installed and in PATH"
    except subprocess.SubprocessError as e:
        return f"Error executing command: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# @mcp.tool()
# def xo_harbor_login() -> str:
#     """
#     Log in to Harbor using username and password from environment variables.
#     Environment variables:
#       - harbor_username
#       - harbor_password
#     """
#     import subprocess
#     username = os.getenv("harbor_username")
#     password = os.getenv("harbor_password")
#     if not username or not password:
#         return "harbor_username or harbor_password environment variable not set."
#     try:
#         result = subprocess.run([
#             'docker', 'login', 'registry.xo.builders', '-u', username, '-p', password
#         ], capture_output=True, text=True)
#         if result.returncode == 0:
#             return result.stdout
#         else:
#             return f"Error running docker login: {result.stderr}"
#     except FileNotFoundError:
#         return "Docker command not found. Please ensure Docker is installed and in PATH."
#     except subprocess.SubprocessError as e:
#         return f"Error executing command: {str(e)}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"

# @mcp.tool()
# def xo_harbor_build_image(project_name: str, image_name: str) -> str:
#     """
#     Build a Harbor image with the tag registry.xo.builders/xoeliza/agentv1 .
#     Equivalent to: docker build -t registry.xo.builders/xoeliza/agentv1 .
#     """
#     import subprocess
#     try:
#         result = subprocess.run([
#             'docker', 'build', '-t', f'registry.xo.builders/{project_name}/{image_name}', '.'
#         ], capture_output=True, text=True)
#         if result.returncode == 0:
#             return result.stdout
#         else:
#             return f"Error running docker build: {result.stderr}"
#     except FileNotFoundError:
#         return "Docker command not found. Please ensure Docker is installed and in PATH."
#     except subprocess.SubprocessError as e:
#         return f"Error executing command: {str(e)}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"

# @mcp.tool()
# def xo_harbor_push_image(project_name: str, image_name: str) -> str:
#     """
#     Push the Harbor image 'registry.xo.builders/xoeliza/agentv1' to the registry.
#     Equivalent to: docker push registry.xo.builders/xoeliza/agentv1
#     """
#     import subprocess
#     try:
#         result = subprocess.run([
#             'docker', 'push', f'registry.xo.builders/{project_name}/{image_name}'
#         ], capture_output=True, text=True)
#         if result.returncode == 0:
#             return result.stdout
#         else:
#             return f"Error running docker push: {result.stderr}"
#     except FileNotFoundError:
#         return "Docker command not found. Please ensure Docker is installed and in PATH."
#     except subprocess.SubprocessError as e:
#         return f"Error executing command: {str(e)}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"

# def get_registry_details(deployment_token: str) -> dict:
#     """
#     Get the registry details from the db using endpoint
#     Arg: deployment_token 
#     """
#     return {}

# @mcp.tool()
# def deploy_to_xo(deployment_token: str) -> str:
#     # fetch the project details from the db
#     details = get_registry_details(deployment_token)
#     project_name = details['project_name']
#     image_name = details['image_name']
    
#     # login to harbor
#     xo_harbor_login()

#     # build the image
#     xo_harbor_build_image(project_name, image_name)

#     # push the image
#     xo_harbor_push_image(project_name, image_name)

@mcp.tool()
def xo_expose_k8s_app(
    # workspace_name: str, 
    # app_name: str, 
    # domain_name: str, 
    # target_port: int
    ) -> str:
    """
    Expose the k8s app to the domain name by calling the /expose-k8s-app endpoint
    """
    import requests
    import os
    
    
    url = f"{backend_url}/expose-k8s-app"
    headers = {
        "Content-Type": "application/json",
        "Access-Token": os.getenv("ACCESS_TOKEN")
    }

    deployment_id = os.getenv("DEPLOYMENT_ID") or None
    if not deployment_id:
        return "DEPLOYMENT_ID environment variable is not set"

    data = {
        # "workspace_name": workspace_name,
        # "app_name": app_name, 
        # "domain_name": domain_name,
        # "target_port": target_port
        "DEPLOYMENT_ID": deployment_id
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
    
