from mcp.server.mcpserver import MCPServer
import json

mcp = MCPServer("BugTracker")


with open("bugs.json", "r", encoding="utf-8") as file:
    bugs = json.load(file)



@mcp.tool()
def get_bugs() -> list[str]:
    """Return the list of reported bugs.""" # docstring — описание функции
    return bugs


@mcp.tool()
def add_bug(description: str) -> str:
    """Add a new bug to the list."""
    bugs.append(description)
    with open("bugs.json", "w", encoding="utf-8") as file:
        json.dump(bugs, file, indent=4)
    return 'Bug added: ' + description + ''


#todo remove_bugs() ?
#todo resolve_bugs()
#todo save result as json

mcp.run()





#основная идея MCP — отделить логику AI-агента от конкретных программ и сервисов, с которыми он работает.

#научиться принимать аргументы от Hermes, а затем хранить баги в JSON, чтобы они не исчезали после перезапуска сервера.


#todo  путь "bugs.json" зависит от текущей рабочей директории. Поскольку Hermes запускает Python как отдельный процесс, позже мы обязательно исправим это через pathlib.Path(__file__), чтобы файл всегда находился рядом с server.py.