"""Main entry point for sys-mcp."""

import logging
from src.server import create_server


logger = logging.getLogger(__name__)

logger.info("Starting SysMCP server...")

if __name__ == "__main__":
    server = create_server()
    logger.info("Starting SysMCP server...")
    server.run(transport="stdio")
