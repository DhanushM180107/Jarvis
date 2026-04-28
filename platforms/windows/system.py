from core.interfaces.system import SystemInterface
from typing import Dict, Any

try:
    import psutil
except ImportError:
    pass

class WindowsSystem(SystemInterface):
    def get_battery_info(self) -> Dict[str, Any]:
        try:
            battery = psutil.sensors_battery()
            if battery:
                return {
                    "percent": battery.percent,
                    "power_plugged": battery.power_plugged
                }
        except Exception:
            pass
        return {"percent": 0, "power_plugged": False}

    def get_cpu_usage(self) -> float:
        try:
            return psutil.cpu_percent(interval=0.5)
        except Exception:
            return 0.0

    def get_memory_usage(self) -> float:
        try:
            return psutil.virtual_memory().percent
        except Exception:
            return 0.0
