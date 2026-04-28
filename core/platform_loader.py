import platform
import importlib
from typing import Any

from core.interfaces.audio import AudioInterface
from core.interfaces.system import SystemInterface
from core.interfaces.notifications import NotificationInterface

class PlatformManager:
    """Dynamically loads platform-specific implementations based on OS."""
    
    def __init__(self):
        self.os_name = platform.system().lower()
        self.audio: AudioInterface = self._load_module('audio', 'Audio')
        self.system: SystemInterface = self._load_module('system', 'System')
        self.notifications: NotificationInterface = self._load_module('notifications', 'Notification')

    def _load_module(self, interface_name: str, class_suffix: str) -> Any:
        try:
            if self.os_name == 'windows':
                module = importlib.import_module(f'platforms.windows.{interface_name}')
                class_name = f"Windows{class_suffix}"
                return getattr(module, class_name)()
            elif self.os_name == 'linux':
                module = importlib.import_module(f'platforms.linux.{interface_name}')
                class_name = f"Linux{class_suffix}"
                return getattr(module, class_name)()
            else:
                raise NotImplementedError(f"Unsupported OS: {self.os_name}")
        except Exception as e:
            print(f"Failed to load {interface_name} for {self.os_name}: {e}")
            return None
