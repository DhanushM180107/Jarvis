import subprocess
import os
from core.interfaces.notifications import NotificationInterface

class LinuxNotification(NotificationInterface):
    def send_notification(self, title: str, message: str) -> bool:
        if not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
            print(f"[Terminal Alert] {title}: {message}")
            return False
            
        try:
            # Using notify-send which is standard on most Linux DEs
            subprocess.run(
                ['notify-send', title, message], 
                check=True, 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            return True
        except Exception as e:
            print(f"Failed to send GUI notification on Linux: {e}")
            return False
