"""Main entry point for sys-mcp."""

import logging
from sys_mcp.server import create_server


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    server = create_server()
    server.run(transport="stdio")
