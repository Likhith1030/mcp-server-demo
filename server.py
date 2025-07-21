import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Shell Access MCP")

@mcp.tool()
def run_shell(command: str) -> str:
    
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.output.strip()}"

@mcp.prompt()
def explain_command_usage(command: str) -> str:
    """
    Suggest a use-case for a given shell command.
    """
    return f"Explain what the '{command}' command does and show an example usage."
