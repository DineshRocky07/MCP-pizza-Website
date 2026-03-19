# MCP-pizza-Website

1. create sever.py 
2. main that server call and run steps mcp.run if code run this pass 
3. mcp.json this will have power to call ai and auto run ai this help

steps day 1:

1.VS Code reads mcp.json, which configures the "pizza MCP" server.
2.When activated, VS Code runs the command uv run main.py.
3.main.py imports the MCP server from server.py and executes mcp.run().
4.server.py starts the FastMCP server named "pizza MCP" with a test tool that returns "Hello from MCP!".
5.The server listens for MCP protocol requests, allowing AI tools to invoke the test tool.