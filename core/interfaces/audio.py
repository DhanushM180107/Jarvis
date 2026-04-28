from abc import ABC, abstractmethod

class AudioInterface(ABC):
    @abstractmethod
    def set_volume(self, level: int) -> bool:
        """Set the system volume to a specific level (0-100)."""
        pass

    @abstractmethod
    def get_volume(self) -> int:
        """Get the current system volume level (0-100)."""
        pass
    
    @abstractmethod
    def speak(self, text: str) -> None:
        """Convert text to speech."""
        pass
