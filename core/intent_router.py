from core.tool_executor import ToolExecutor

class IntentRouter:
    def __init__(self, executor: ToolExecutor):
        self.executor = executor

    def route(self, intent: str, parameters: dict):
        # Basic intent mapping - in a real app this would use NLP
        tool_mapping = {
            "set_volume": "SetVolume",
            "get_battery": "GetBattery",
            "notify": "SendNotification"
        }
        
        tool_name = tool_mapping.get(intent)
        if tool_name:
            print(f"Routing intent '{intent}' to tool '{tool_name}' with args {parameters}")
            return self.executor.execute(tool_name, **parameters)
        return "Unknown intent."
