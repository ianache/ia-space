import anyio
import click
import mcp.types as types
from mcp.server.lowlevel import Server
from ..template_server import TemplatesServer


TOOLS = [
    types.Tool(
        name="poem",
        description="Writing a poem.",
        inputSchema={
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic of the poem",
                },
            },
            "required": ["topic"]
        },
    )
]

@click.command()
@click.option("--port", default=8000, help="Port to listen on for SSE")
@click.option(
    "--transport",
    type=click.Choice(["stdio", "sse"]),
    default="stdio",
    help="Transport type",
)
def main(port: int, transport: str) -> int:
    app = Server("mcp-simple-prompt")
    template_loader = TemplatesServer()

    @app.list_prompts()
    async def list_prompts() -> list[types.Prompt]:
        prompts = []
        for name, data in template_loader.templates.items():
            config = data.get("config", {})
            prompt_args = [
                types.PromptArgument(
                    name=arg.get("name"),
                    description=arg.get("description"),
                    required=arg.get("required", False),
                )
                for arg in config.get("arguments", [])
            ]
            prompts.append(
                types.Prompt(
                    name=name,
                    description=config.get("description", ""),
                    arguments=prompt_args,
                )
            )
        return prompts
    
    @app.get_prompt()
    async def get_prompt(
        name: str, arguments: dict[str, str] | None = None # Arguments are not used yet but might be in the future
    ) -> types.GetPromptResult:
        template_data = template_loader.get_template(name)
        if template_data is None:
            raise ValueError(f"Unknown prompt: {name}")

        prompt_text = template_data.get("prompt_text", "")
        config = template_data.get("config", {})
        description = config.get("description", "")

        # TODO: Handle argument substitution in prompt_text if needed in the future
        # For now, we pass the raw prompt_text
        
        return types.GetPromptResult(
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(type="text", text=prompt_text),
                )
            ],
            description=description,
        )

    @app.call_tool()
    async def call_tool(
        name: str, 
        parameters: dict[str, str]
    ) -> dict:
        # Handle the "poem" tool
        if name == "poem":
            topic = parameters.get("topic", None)
            return {
                "result": f"Here is a poem about {topic}."
            }
        else:
            raise ValueError(f"Unknown tool: {name}")

    @app.list_tools()
    async def list_tools() -> list[str]:
        return TOOLS
    
    if transport == "sse":
        from mcp.server.sse import SseServerTransport
        from starlette.applications import Starlette
        from starlette.responses import Response
        from starlette.routing import Mount, Route

        sse = SseServerTransport("/messages/")

        async def handle_sse(request):
            async with sse.connect_sse(
                request.scope, request.receive, request._send
            ) as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )
            return Response()

        starlette_app = Starlette(
            debug=True,
            routes=[
                Route("/sse", endpoint=handle_sse),
                Mount("/messages/", app=sse.handle_post_message),
            ],
        )

        import uvicorn

        uvicorn.run(starlette_app, host="0.0.0.0", port=port)
    else:
        from mcp.server.stdio import stdio_server

        async def arun():
            async with stdio_server() as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )

        anyio.run(arun)

    return 0