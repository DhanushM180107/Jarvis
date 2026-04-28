import subprocess
from core.interfaces.audio import AudioInterface

try:
    import pulsectl
except ImportError:
    pass

class LinuxAudio(AudioInterface):
    def set_volume(self, level: int) -> bool:
        try:
            level = max(0, min(100, level))
            with pulsectl.Pulse('volume-control') as pulse:
                sinks = pulse.sink_list()
                if not sinks:
                    return False
                # Assuming default sink is the first one
                pulse.volume_set_all_chans(sinks[0], level / 100.0)
            return True
        except Exception as e:
            print(f"Failed to set volume on Linux: {e}")
            return False

    def get_volume(self) -> int:
        try:
            with pulsectl.Pulse('volume-control') as pulse:
                sinks = pulse.sink_list()
                if not sinks:
                    return 0
                return int(sinks[0].volume.value_flat * 100)
        except Exception:
            return 0

    def speak(self, text: str) -> None:
        try:
            # Using espeak for Linux TTS
            subprocess.run(['espeak', text], check=True)
        except Exception as e:
            print(f"Failed to speak on Linux: {e}")
