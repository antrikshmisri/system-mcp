"""Main entry point for sys-mcp."""

import logging
from sys_mcp.server import create_server


logger = logging.getLogger(__name__)


def main():
    """Main function to run the sys-mcp server."""
    server = create_server()
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
