import sys
import os

# Ensure the root directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.platform_loader import PlatformManager
from Brain.personality import jarvis_speak

platform_manager = PlatformManager()

def get_volume_windows():
    if platform_manager.audio:
        current_volume = platform_manager.audio.get_volume()
        jarvis_speak(f"Current volume level is {current_volume}%.")
    else:
        jarvis_speak("Audio interface is not available.")

def set_volume_windows(percentage):
    if platform_manager.audio:
        platform_manager.audio.set_volume(percentage)
        jarvis_speak(f"Volume set to {percentage}%")
    else:
        jarvis_speak("Audio interface is not available.")
