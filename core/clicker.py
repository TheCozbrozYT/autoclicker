import pyautogui
import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DEFAULT_CLICK_SPEED, DEFAULT_RANDOM_POSITION

class AutoClicker:
    def __init__(self):
        pyautogui.PAUSE = 0
        self.state = False
        self.click_speed = DEFAULT_CLICK_SPEED
        self.random_position = DEFAULT_RANDOM_POSITION

    def toggle(self):
        self.state = not self.state
        return self.state

    def set_speed(self, speed):
        self.click_speed = float(speed)

    def set_random_position(self, enabled):
        self.random_position = enabled

    def stop(self):
        self.state = False

    def click(self):
        if self.random_position:
            x = random.randint(0, pyautogui.size().width)
            y = random.randint(0, pyautogui.size().height)
            pyautogui.mouseDown(x, y)
            pyautogui.mouseUp(x, y)
        else:
            pyautogui.mouseDown()
            pyautogui.mouseUp()
