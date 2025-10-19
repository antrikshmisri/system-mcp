# sys-mcp

A small MCP server that exposes basic system commands for UNIX-like environments. Works with Claude Desktop or any MCP-compatible client.

## Requirements

* Python 3.11 or newer
* [uv](https://docs.astral.sh/uv/) for dependency management
* UNIX-like system (macOS, Linux, BSD)

## Usage

```bash
uv run python -m src
```

Or add it to your MCP config:

```json
{
  "mcpServers": {
    "sys-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/sys-mcp",
        "run",
        "python",
        "-m",
        "src"
      ]
    }
  }
}
```

## Notes

* Runs over stdio, no network required
* Logs to stdout
* Blocks unsafe commands by default

You can test it with Claude Desktop by following [these steps](https://modelcontextprotocol.io/docs/develop/build-server#testing-your-server-with-claude-for-desktop).
