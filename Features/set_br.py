try:
    import wmi
except ImportError:
    wmi = None

from Brain.personality import jarvis_speak

def set_brightness_windows(percentage):
    if wmi is None:
        jarvis_speak("Brightness control is not supported on this operating system.", mood="error")
        return
    try:
        w = wmi.WMI(namespace='wmi')
        brightness_methods = w.WmiMonitorBrightnessMethods()[0]
        brightness_methods.WmiSetBrightness(int(percentage), 0)
        jarvis_speak(f"Brightness set to {percentage}%.")
    except Exception as e:
        jarvis_speak(f"Error adjusting brightness: {e}", mood="error")
