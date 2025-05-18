from fastmcp import FastMCP, Context
from fastmcp.prompts.prompt import Prompt
import uvicorn
import os
import yaml
import mcp.types as types
import asyncio
#from services import DeviceService
from config import configuration

class TemplatesServer():
    def __init__(self):
        self.templates = self._load_templates()

    def _load_templates(self):
        templates = {}
        templates_path = os.path.join(os.path.dirname(__file__), "templates")
        for category in os.listdir(templates_path):
            category_path = os.path.join(templates_path, category)
            if category in os.listdir(category_path):
                # Load config
                with open(os.path.join(category_path, "config.yaml"), "r") as file:
                    config = yaml.safe_load(file)
                with open(os.path.join(category_path, "template.md"), "r") as file:
                    template = file.read()
                
                templates[category] = {
                    "config": config,
                    "template": template
                }
        return templates
                 
    def get_template(self, name):
        return self.templates.get(name)

templates_server = TemplatesServer()

version = "0.1.0"
mcp = FastMCP(name="MCP Prompts")

@mcp.resource("config://version")
def get_version(): 
    return version

@mcp.get_prompts( )
async def get_prompts() -> dict[str, Prompt]: #list[types.Prompt]:
    """List all available prompts"""
    prompts = []
    for name, template in templates_server.templates.items():
        prompts.append(
            types.Prompt(
                name=name,
                description=template["config"]["description"],
                arguments=template["config"]["arguments"],
            )
        )
    return prompts

@mcp.prompt()
async def get_prompt(name: str, arguments: dict[str, str] | None, ctx: Context) -> types.GetPromptResult:
    """Get a prompt template"""
    if name not in templates_server.templates:
        raise ValueError(f"Template {name} not found")
    # Fetch the template
    template = templates_server.templates[name]
    formatted_template = template["template"]
    if arguments:
        for key,value in arguments.items():
            formatted_template = formatted_template.replace(f"{{{{ {key} }}}}", value)
    return types.GetPromptResult(
        description=template["config"]["description"],
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(
                    type="test",
                    text=formatted_template
                )
            )
        ]
    )

mcp.run(
    transport=configuration.MCP_TRANSPORT, 
    host=configuration.MCP_HOST, 
    port=configuration.MCP_PORT, 
    path="/mcp"
)