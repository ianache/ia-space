# ia-space
Espacio de proyectos relacionados a IA

```Powersheel
irm https://astral.sh/uv/install.ps1 | iex
```

## MCP Servers

Se han creado los proyectos para los servicios usando el siguiente comando

```sh
uv init mvp-gitlab
uv init mcp-devices
uv init mcp-units
```

### Manage Gitlab

Este servidor de MCP permite gestionar operaciones sobre GitLab.

# Probar servidores

```sh
uv run fastmcp  run main.py:mcp
```

```sh
npx @modelcontextprotocol/inspector
```

Acceder a URL: http://127.0.0.1:6274