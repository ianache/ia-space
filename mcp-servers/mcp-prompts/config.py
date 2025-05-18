import os 
import logging

class Config:
    def __init__(self):
        self.MCP_PORT = int(os.getenv("PORT", 8001))
        self.MCP_HOST = os.getenv("HOST", "0.0.0.0")
        self.MCP_TRANSPORT = os.getenv("TRANSPORT", "sse") #"streamable-http")
        self.MCP_PATH = os.getenv("MCP_PATH", "/mcp")
        # Config for Logging
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


configuration = Config()
logging.basicConfig(level=logging.INFO)