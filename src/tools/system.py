"""MCP tools for system control and information."""

import logging
import yaml
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Set
from src.tools import MCPToolGroup
from mcp.server.fastmcp import FastMCP


logger = logging.getLogger(__name__)


def _read_blacklisted_commands() -> Set[str]:
    """Read the blacklisted commands from the YAML file.

    Returns:
        A set of blacklisted command names.
    """
    blacklist_path = Path(__file__).parent.parent / "data" / "blacklist.yml"

    with open(blacklist_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return set(data.get("blacklisted", []))


BLACKLISTED_COMMANDS: Set[str] = _read_blacklisted_commands()


def _is_command_safe(command: str) -> bool:
    """Check if a command is safe to execute.

    Args:
        command: The command to check.

    Returns:
        True if the command is safe, False otherwise.
    """
    return command.split()[0] not in BLACKLISTED_COMMANDS


class SystemToolGroup(MCPToolGroup):
    """Tool group for system-related MCP tools."""

    def __init__(self, server: FastMCP) -> None:
        super().__init__(server, group_name="system")

    @staticmethod
    def execute_command(command: str) -> str:
        """Execute a system command if it is safe.

        Args:
            command: The system command to execute.

        Returns:
            The output of the command or an error message.
        """
        if not _is_command_safe(command):
            return f"Error: Command '{command}' is blacklisted and cannot be executed."

        proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode != 0:
            return f"Error: Command '{command}' failed with error:\n{stderr.decode()}"

        return stdout.decode()

    @staticmethod
    def system_stats() -> str:
        """Retrieve basic system statistics.

        Returns:
            A string containing system statistics.
        """
        proc = Popen("top -l 1 | head -n 10", shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode != 0:
            return f"Error: Failed to retrieve system stats:\n{stderr.decode()}"

        return stdout.decode()

    def register_tools(self) -> None:
        """Register system mcp tools. Registers:

        - exec_cmd: Execute a system command.
        - sys_stats: Retrieve basic system statistics.
        """
        logger.info("Registering system tools...")
        self.server.tool(
            name="execute_command",
            description="Execute a system command.",
        )(self.execute_command)

        self.server.tool(
            name="system_stats",
            description="Retrieve basic system statistics.",
        )(self.system_stats)
