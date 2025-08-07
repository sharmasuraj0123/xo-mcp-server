from .xo_mcp_server import mcp
from .web_server import run_server

def main() -> None:
    print("Hello from xo-mcp-server!")
    # Run the web server instead of the direct MCP server
    run_server(host="0.0.0.0", port=5000)
