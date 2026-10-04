import pyautogui
pyautogui.FAILSAFE = True
import time


# mouse opeations
pyautogui.moveTo(100, 100, duration=1)
# Mouse click
pyautogui.rightClick(100,100, duration=1)
time.sleep(1)
pyautogui.moveTo(900,700, duration=1)
#scroll functions
pyautogui.click(900,800, duration=1)
pyautogui.scroll(500)
pyautogui.scroll(-500)
time.sleep(1)