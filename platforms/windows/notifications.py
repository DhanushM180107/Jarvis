from core.interfaces.notifications import NotificationInterface

try:
    from winotify import Notification
except ImportError:
    pass

class WindowsNotification(NotificationInterface):
    def send_notification(self, title: str, message: str) -> bool:
        try:
            toast = Notification(app_id="AIAssistant", title=title, msg=message)
            toast.show()
            return True
        except Exception as e:
            print(f"Failed to send notification on Windows: {e}")
            return False
