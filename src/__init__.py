"""MCP server for any UNIX-like system eg. Linux, BSD, macOS."""

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stderr)],
)
