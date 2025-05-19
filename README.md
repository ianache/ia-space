# ia-space
Espacio de proyectos relacionados a IA

## Requisitos

Se debe tener instalado los siguientes productos:
- Oracle VirtualBox
- Hashicorp Vagrant
- Microsoft Visual Studio Code + Copilot

Se debe instalar Python y contar con librerias instaladas. Para ello se recomienda ejecutar:

- Powersheel de Windows
- Instalar gestor de paquetes Python `uv`
```Powersheel
irm https://astral.sh/uv/install.ps1 | iex
```

## Iniciar entorno virtual

```sh
vagrant up
```

## MCP Servers

Se han creado los proyectos para los servicios usando el siguiente comando

```sh
uv init mvp-gitlab
uv init mcp-devices
uv init mcp-units
uv init 
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

# Servidores MCP integrados a IDE Visual Studio COde

## Playwright (interacción con exploradores Web)

```sh
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```
