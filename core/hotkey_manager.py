import keyboard
import time
from threading import Thread
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import HOTKEY_TOGGLE

class HotkeyManager:
    def __init__(self, toggle_callback):
        self.toggle_callback = toggle_callback
        self.running = True

    def start(self):
        self.thread = Thread(target=self._check_hotkeys, daemon=True)
        self.thread.start()

    def _check_hotkeys(self):
        while self.running:
            if keyboard.is_pressed(HOTKEY_TOGGLE):
                self.toggle_callback()
            time.sleep(0.05)