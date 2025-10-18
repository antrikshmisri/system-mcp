"""Module to define system-related MCP server."""

import logging
from mcp.server.fastmcp import FastMCP
from src.tools.system import SystemToolGroup


logger = logging.getLogger(__name__)


_INSTRUCTIONS = """
You are a system management MCP server designed to help users manage and interact with UNIX-like systems.
You can execute safe to run system commands and retrieve system information.
"""
logger.info("Creating SysMCP server instance...")


def create_server() -> FastMCP:
    """Create and return a FastMCP server instance.

    Returns:
        An instance of FastMCP.
    """
    logger.info("Creating SysMCP server instance...")

    server = FastMCP(
        name="SysMCP",
    )

    SystemToolGroup(server).register_tools()

    return server
