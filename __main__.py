#!/usr/bin/env python3
"""
Entry point for ESP RainMaker MCP Server.
This module serves as the main entry point when the package is executed.
"""

import sys
import os

# Add the current directory to sys.path to find server.py
sys.path.insert(0, os.path.dirname(__file__))

# Import and run the server
import server

if __name__ == "__main__":
    # If executed directly, this should be invoked via mcp run
    print("Please use 'mcp run server.py' to start the server.")
    sys.exit(1)

def main():
    """Main entry point for the package."""
    print("Please use 'mcp run server.py' to start the server.")
    sys.exit(1)