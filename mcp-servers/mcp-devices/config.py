import os 
import logging

class Config:
    def __init__(self):
        self.MCP_PORT = int(os.getenv("PORT", 8000))
        self.MCP_HOST = os.getenv("HOST", "0.0.0.0")
        self.MCP_TRANSPORT = os.getenv("TRANSPORT", "sse") #"streamable-http")
        # Config for API Service
        self.API_BASEURL = os.getenv("API_BASEURL", "http://localhost:8000")
        self.API_USERNAME = os.getenv("API_USERNAME", "admin")
        self.API_PASSWORD = os.getenv("API_PASSWORD", "admin")
        self.API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET", "secret")
        # Keycloak Config
        self.KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "https://oauth.dev.comsatel.com.pe")
        self.KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "microservices")
        # Config for Logging
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


configuration = Config()
logging.basicConfig(level=logging.INFO)