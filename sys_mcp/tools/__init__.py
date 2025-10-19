"""Tools for sys-mcp."""

from abc import ABC, abstractmethod
from mcp.server.fastmcp import FastMCP


class MCPToolGroup(ABC):
    """Abstract base class for MCP tool groups."""

    def __init__(self, server: FastMCP, group_name: str) -> None:
        self.server = server
        self.group_name = group_name

    @abstractmethod
    def register_tools(self) -> None:
        """Register the tools in this group."""
        raise NotImplementedError("register_tools must be implemented by subclasses")


__all__ = ["MCPToolGroup"]
