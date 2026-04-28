from core.tool_registry import ToolRegistry
from typing import Any

class ToolExecutor:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, tool_name: str, **kwargs) -> Any:
        tool = self.registry.get_tool(tool_name)
        if tool:
            try:
                return tool(**kwargs)
            except Exception as e:
                return f"Error executing {tool_name}: {e}"
        return f"Tool {tool_name} not found."
