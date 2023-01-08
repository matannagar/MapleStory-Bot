import pyautogui
import time

pyautogui.FAILSAFE = True

class NoKeyboardException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "No On-Screen Keyboard found. Try redo-ing your screenshot."

class Bot():
    def __init__(self):
        self.osk = pyautogui.locateOnScreen('keyBoard.png',grayscale=True, confidence=.5)
        if self.osk is None:
            raise NoKeyboardException()

    def _moveTo(self, coord):
        pyautogui.moveTo(self.osk[0] + coord[0], self.osk[1] + coord[1])

    def click(self, key, duration, clicks=1):
        pyautogui.click(self.osk[0] + key[0], self.osk[1] + key[1],
        duration=duration, clicks=clicks)
        time.sleep(0.25)
        # self._moveTo(key)
        # pyautogui.mouseDown()
        # time.sleep(duration)
        # pyautogui.mouseUp()
