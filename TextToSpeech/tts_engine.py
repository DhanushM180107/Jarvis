import threading
import sys
import os

# Ensure the root directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.platform_loader import PlatformManager

platform_manager = PlatformManager()

# Global lock to prevent overlapping audio
_audio_lock = threading.Lock()

def speak(text: str):
    """
    Converts text to speech and plays it locally using cross-platform capabilities.
    """
    if not text or not text.strip():
        return

    # Use lock to ensure only one sentence is spoken at a time
    with _audio_lock:
        if platform_manager.audio:
            platform_manager.audio.speak(text)
        else:
            print(f"TTS Engine not available. Would have said: {text}")

if __name__ == "__main__":
    print("Testing TTS Engine...")
    speak("System initialization complete. Jarvis is ready.")
