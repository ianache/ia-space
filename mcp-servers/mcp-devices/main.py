from fastmcp import FastMCP, Context
import uvicorn
import os
from services import DeviceService
from config import configuration

version = "0.1.0"
mcp = FastMCP(name="MCP Devices")

service = DeviceService(configuration)

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
    return service.add_device (
        imei=imei, 
        obc="1234567890", 
        linenumber="1234567890", 
        operator="CLARO"
    )

@mcp.tool(name="remove_device", description="Remove a device")
async def remove_device(imei: str, ctx: Context) -> str:
    """Remove a device (GPS, Dashcam, etc.)"""
    await ctx.info(f"Processing {imei}...")
    return { 
        "id": "22222222222", 
        "message": "Device removed successfully" 
    }

@mcp.tool(name="get_device", description="Get device information")
async def get_device(imei: str, ctx: Context) -> str:
    """Get device information (GPS, Dashcam, etc.)"""
    await ctx.info(f"Processing {imei}...")
    return service.get_device (id=imei)

mcp.run(
    transport=configuration.MCP_TRANSPORT, 
    host=configuration.MCP_HOST, 
    port=configuration.MCP_PORT, 
    path="/mcp"
)