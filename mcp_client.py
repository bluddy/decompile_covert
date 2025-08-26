#!/usr/bin/env python3
#
# A simple interactive command-line client for the IDA Pro MCP JSON-RPC server.
#
# This client helps you connect to and debug the MCP server running inside IDA Pro.
#
# Usage:
#   python mcp_client.py [server_url]
#
#   If server_url is not provided, it defaults to http://localhost:13337/mcp.
#
# Dependencies:
#   - requests: `pip install requests`
#
# Example session:
# > help
# > get_metadata
# > list_functions 0 5
# > disassemble_function "main"
#

import json
import sys
import shlex

try:
    import readline
except ImportError:
    # readline is not available on Windows by default
    pass

try:
    import requests
except ImportError:
    print("The 'requests' library is not installed.", file=sys.stderr)
    print("Please install it using: pip install requests", file=sys.stderr)
    sys.exit(1)


class MCPClient:
    """An interactive client for the IDA MCP JSON-RPC server."""

    def __init__(self, url="http://localhost:13337/mcp"):
        self.url = url
        self.request_id = 1

    def send_request(self, method, params):
        """Constructs and sends a JSON-RPC request."""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.request_id,
        }
        self.request_id += 1

        try:
            response = requests.post(self.url, json=payload, timeout=20)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON response", "raw_response": response.text}

    def run(self):
        """Runs the main interactive loop (REPL)."""
        print("MCP Interactive Client")
        print(f"Connecting to: {self.url}")
        print("Type 'help' for commands, 'quit' or 'exit' to leave.")

        while True:
            try:
                line = input("> ").strip()
                if not line:
                    continue

                parts = shlex.split(line)
                if not parts:
                    continue

                command = parts[0].lower()

                if command in ("quit", "exit"):
                    break
                elif command == "help":
                    self.show_help()
                elif command == "url":
                    if len(parts) > 1:
                        self.url = parts[1]
                        print(f"Server URL set to: {self.url}")
                    else:
                        print(f"Current server URL: {self.url}")
                else:
                    # It's an RPC call
                    method = parts[0]
                    params = self.parse_params(parts[1:])
                    response = self.send_request(method, params)
                    print(json.dumps(response, indent=2))

            except (EOFError, KeyboardInterrupt):
                print("\nExiting.")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}", file=sys.stderr)

    def show_help(self):
        """Displays the client's help message."""
        print("\nClient Commands:")
        print("  <method> [param1] [param2] ... - Call a JSON-RPC method.")
        print("  url [new_url]                  - Show or set the server URL.")
        print("  help                           - Show this help message.")
        print("  quit / exit                    - Exit the client.\n")
        print("Example RPC call: get_metadata")
        print("Example with params: list_functions 0 10")
        print("Example with quoted string: rename_function 0x1234 \"my_new_func_name\"")

    def parse_params(self, str_params):
        """Tries to convert params to int/float, otherwise leaves as string."""
        return [p for p in str_params]

if __name__ == "__main__":
    server_url = "http://localhost:13337/mcp"
    if len(sys.argv) > 1:
        server_url = sys.argv[1]

    client = MCPClient(server_url)
    client.run()