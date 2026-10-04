import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Step 1: Opening Chrome browser...")
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('chrome', interval=0.05)
time.sleep(1)
pyautogui.press('enter')

pyautogui.press('tab')
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

#open new tab in the brower
pyautogui.hotkey('ctrl', 't')
time.sleep(1)

#open the BBC weather website
pyautogui.write('https://www.bbc.com/weather/1264527', interval=0.05)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

print("Step 2: BBC weather website opened successfully.")

#copying the data from the website.
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

print("Step 3: Data copied successfully.")  

# Opening Notepad to paste the copied data
import os
import subprocess
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

print("Step 4: Notepad opened successfully.")

# Create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Get project folder
project_folder = os.path.dirname(os.path.abspath(__file__))

# Create complete file path
filename = f"BBC_Weather_{datetime.now().strftime('%d_%m_%Y %I_%M%p')}.txt"
file_path = os.path.join(project_folder, filename)

print("Saving file to:")
print(file_path)

#paste the copied data into Notepad
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)


# Open Save dialog
pyautogui.hotkey('ctrl', 's')
time.sleep(2)

# Enter complete file path
pyautogui.write(file_path, interval=0.03)
time.sleep(1)


# Save
pyautogui.press('enter')
time.sleep(2)

print("File saved successfully!")

#close the notepad
pyautogui.hotkey('alt', 'f4')
time.sleep(1)

#close the tab in the browser
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)

print("Step 5: Browser tab closed successfully.")

pyautogui.hotkey('alt', 'tab')
time.sleep(1)

print("Automation completed successfully!")

    


