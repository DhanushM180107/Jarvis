from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    @abstractmethod
    def send_notification(self, title: str, message: str) -> bool:
        """Send a system notification."""
        pass
