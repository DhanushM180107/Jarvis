import sys
import os

# Ensure the root directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.platform_loader import PlatformManager
from core.tool_registry import ToolRegistry
from core.tool_executor import ToolExecutor
from core.intent_router import IntentRouter

def main():
    print("Initializing Platform Layer...")
    platform_manager = PlatformManager()
    
    if platform_manager.audio:
        platform_manager.audio.speak("Initializing cross platform assistant.")
        
    print("Setting up Tool Registry...")
    registry = ToolRegistry()
    
    # Registering tools that use the platform-agnostic interfaces
    def set_volume_tool(level: int):
        if platform_manager.audio:
            success = platform_manager.audio.set_volume(level)
            return "Volume set successfully." if success else "Failed to set volume."
        return "Audio interface not available."
        
    def get_battery_tool():
        if platform_manager.system:
            return platform_manager.system.get_battery_info()
        return "System interface not available."
        
    def send_notification_tool(title: str, message: str):
        if platform_manager.notifications:
            success = platform_manager.notifications.send_notification(title, message)
            return "Notification sent." if success else "Failed to send notification."
        return "Notification interface not available."

    registry.register("SetVolume", set_volume_tool)
    registry.register("GetBattery", get_battery_tool)
    registry.register("SendNotification", send_notification_tool)
    
    executor = ToolExecutor(registry)
    router = IntentRouter(executor)
    
    # Example interactions
    print("\n--- Testing Assistant Routing ---")
    
    # 1. Ask for Battery
    print("User: 'What is my battery level?'")
    result = router.route("get_battery", {})
    print(f"Assistant: {result}")
    
    # 2. Set Volume
    print("\nUser: 'Set volume to 50%'")
    result = router.route("set_volume", {"level": 50})
    print(f"Assistant: {result}")
    
    # 3. Send Notification
    print("\nUser: 'Send a test notification'")
    result = router.route("notify", {"title": "Test", "message": "Cross-platform works!"})
    print(f"Assistant: {result}")

if __name__ == "__main__":
    main()
