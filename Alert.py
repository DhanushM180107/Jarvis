import os
import sys

# Ensure the root directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.platform_loader import PlatformManager

platform_manager = PlatformManager()

def Alert(Text):
    if platform_manager.notifications:
        platform_manager.notifications.send_notification("🟢 J.A.R.V.I.S.", Text)
    else:
        print(f"ALERT: {Text}")
