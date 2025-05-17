# Use official Python image with uv pre-installed
FROM python:3.11-slim

# Install uv (if not present in the base image)
RUN pip install uv

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using uv
RUN uv pip install --system --requirement pyproject.toml || true

# Expose the default port
EXPOSE 8000

# Set the entrypoint command
CMD ["uv", "run", "fastmcp", "run", "main.py:mcp"]
