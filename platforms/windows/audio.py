import ctypes
from core.interfaces.audio import AudioInterface

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    import pyttsx3
except ImportError:
    pass

class WindowsAudio(AudioInterface):
    def __init__(self):
        self.tts_engine = None
        try:
            self.tts_engine = pyttsx3.init('sapi5')
        except Exception:
            pass

    def _get_volume_interface(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return cast(interface, POINTER(IAudioEndpointVolume))

    def set_volume(self, level: int) -> bool:
        try:
            volume = self._get_volume_interface()
            # Convert 0-100 to scalar
            scalar_volume = max(0.0, min(1.0, level / 100.0))
            volume.SetMasterVolumeLevelScalar(scalar_volume, None)
            return True
        except Exception as e:
            print(f"Failed to set volume on Windows: {e}")
            return False

    def get_volume(self) -> int:
        try:
            volume = self._get_volume_interface()
            scalar = volume.GetMasterVolumeLevelScalar()
            return int(scalar * 100)
        except Exception:
            return 0

    def speak(self, text: str) -> None:
        if self.tts_engine:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        else:
            print(f"TTS Engine not initialized. Text: {text}")
