from mcp.server.mcpserver import MCPServer
import json

mcp = MCPServer("BugTracker")


with open("bugs.json", "r", encoding="utf-8") as file:
    bugs = json.load(file)






@mcp.tool()
def get_bugs() -> list[str]:
    """Return the list of reported bugs.""" # docstring — описание функции
    return bugs

#todo add_bugs()
@mcp.tool()
def add_bug(description: str) -> str:
    """Add a new bug to the list."""
    bugs.append(description)
    return 'Bug added: ' + description + ''


#todo remove_bugs() ?
#todo resolve_bugs()
#todo save result as json
mcp.run()





#основная идея MCP — отделить логику AI-агента от конкретных программ и сервисов, с которыми он работает.

#научиться принимать аргументы от Hermes, а затем хранить баги в JSON, чтобы они не исчезали после перезапуска сервера.


