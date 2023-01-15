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

    def click(self, key, duration):
        self._moveTo(key)
        pyautogui.mouseDown()
        time.sleep(duration)
        pyautogui.mouseUp()
        # pyautogui.click(duration=duration, clicks=clicks)
        # time.sleep(0.15)
    
    def jump(self, key1, key2, duration):
        self._moveTo(key1)
        pyautogui.mouseDown()
        time.sleep(0.05)
        pyautogui.mouseUp()
        self._moveTo(key2)
        pyautogui.mouseDown()
        time.sleep(duration)
        pyautogui.mouseUp()
    
    def moveChannel():
        pass
        
        
