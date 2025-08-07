from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

TOOLS = [
    {
        "name": "hello_credentials",
        "description": "Echo back the supplied credentials.",
        "parameters": {"type": "object", "properties": {}, "required": []},
    }
]

# ---------- manifest ----------
@app.get("/mcp/manifest")
async def manifest():
    return {
        "version": "2025-08-05",
        "name": "XO Sample MCP",
        "transport": "streamable-http",
        "endpoint": "/mcp",
        "tools": TOOLS,
    }

# ---------- alias so clients that expect /manifest also work ----------
@app.get("/manifest")          # <— add these two lines
async def manifest_alias():    # <— and reuse the existing function
    return await manifest()    # (no code duplication)

# ---------- JSON-RPC ----------
@app.post("/mcp")
async def mcp(
    request: Request,
    authorization: str | None = Header(None),
    x_deployment_id: str | None = Header(None),
):
    body = await request.json()

    if body.get("jsonrpc") != "2.0":
        raise HTTPException(400, "Invalid JSON-RPC version")

    method = body.get("method")

    # ---------- 1) tools/list ----------
    if method == "tools/list":
        return JSONResponse(
            {"jsonrpc": "2.0", "id": body.get("id"), "result": {"tools": TOOLS}}
        )

    # ---------- 2) tools/call ----------
    if method == "tools/call":
        if body["params"]["name"] != "hello_credentials":
            raise HTTPException(400, "Unknown tool")

        # basic auth check
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(401, "Missing Authorization header")
        if not x_deployment_id:
            raise HTTPException(401, "Missing X-Deployment-Id header")

        token = authorization.removeprefix("Bearer ").strip()
        reply = {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": (
                            f"Hello! Your ACCESS_TOKEN is **{token}** and "
                            f"DEPLOYMENT_ID is **{x_deployment_id}**."
                        ),
                    }
                ]
            },
        }
        return JSONResponse(reply)

    # ---------- unsupported ----------
    raise HTTPException(400, f"Unsupported method {method!r}")
