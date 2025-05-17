from fastmcp import FastMCP, Context
import uvicorn
import os

version = "0.1.0"
mcp = FastMCP(name="MyServer")
#http_app = app.http_app()

MCP_PORT    = int(os.getenv("PORT", 8000))
MCP_HOST   = os.getenv("HOST", "0.0.0.0")
MCP_TRANSPORT = os.getenv("TRANSPORT", "sse") #"streamable-http")

@mcp.resource("config://version")
def get_version(): 
    return version

# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: str):
    # Fetch profile for user_id...
    return {"name": f"User {user_id}", "status": "active"}

@mcp.tool(name="add_device", description="Add a new device")
async def add_device(imei: str, ctx: Context) -> str:
    """Add a new device (GPS, Dashcam, etc.)"""
    await ctx.info(f"Processing {imei}...")
    return { "id": "11111111111", "message": "Device added successfully" }

mcp.run(transport=MCP_TRANSPORT, host=MCP_HOST, port=MCP_PORT, path="/mcp")