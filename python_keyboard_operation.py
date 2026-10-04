import pyautogui
import time
import subprocess
import os

'''
#hotkey operations
pyautogui.typewrite('Hello, this is a test message!', interval=0.1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
print("Copy operation performed")
pyautogui.hotkey('ctrl', 'v')
print("Paste operation performed")
'''


# Get current project folder
project_folder = os.path.dirname(os.path.abspath(__file__))

# Create test.txt path
file_path = os.path.join(project_folder, "test.txt")

# Create empty file
with open(file_path, "w") as file:
    pass

print("Opening Notepad...")

# Open test.txt specifically in Notepad
subprocess.Popen(["notepad.exe", file_path])

# Wait for Notepad
time.sleep(3)

# Type text
pyautogui.write(
    "Hello, this is a test message!",
    interval=0.05
)

time.sleep(1)


# Select all
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)

# Copy
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

print("Copy operation performed")

pyautogui.hotkey("esc")

#pressing the enter key to create a new line
pyautogui.press("enter")

# Paste
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

print("Paste operation performed")

# Save
pyautogui.hotkey("ctrl", "s")

print("File saved successfully!")

#taking screenshot of the notepad window
screenshot = pyautogui.screenshot()
screenshot.save("snapshot.png")
