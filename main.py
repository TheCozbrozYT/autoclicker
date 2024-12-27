from core.clicker import AutoClicker
from core.hotkey_manager import HotkeyManager
from gui.app import AutoClickerApp
import threading
import time

def run_clicker(clicker):
    while True:
        if clicker.state:
            clicker.click()
            time.sleep(clicker.click_speed)
        time.sleep(0.005)

def main():
    clicker = AutoClicker()
    app = AutoClickerApp(clicker)
    
    hotkey_manager = HotkeyManager(app.toggle_autoclicker)
    hotkey_manager.start()
    
    clicker_thread = threading.Thread(target=run_clicker, args=(clicker,), daemon=True)
    clicker_thread.start()
    
    app.root.mainloop()

if __name__ == "__main__":
    main()