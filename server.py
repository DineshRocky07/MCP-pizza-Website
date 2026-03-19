from mcp.server.fastmcp import FastMCP

mcp =FastMCP("pizza MCP")

@mcp.tool(
    name="tool test",
    description="A tool for testing the MCP framework.",
)
def say_hello() -> str:
    return "Hello from MCP!"