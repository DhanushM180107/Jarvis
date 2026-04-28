from abc import ABC, abstractmethod
from typing import Dict, Any

class SystemInterface(ABC):
    @abstractmethod
    def get_battery_info(self) -> Dict[str, Any]:
        """Get battery percentage and status."""
        pass

    @abstractmethod
    def get_cpu_usage(self) -> float:
        """Get current CPU usage percentage."""
        pass

    @abstractmethod
    def get_memory_usage(self) -> float:
        """Get current memory usage percentage."""
        pass
