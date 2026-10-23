
import requests  # pip install requests


def is_Online(url="https://www.google.com", timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return 200 <= response.status_code < 300
    except Exception as e:
        print(f"Internet check failed: {e}")
        return False
