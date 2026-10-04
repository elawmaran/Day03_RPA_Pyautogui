import pyautogui
import time
import os
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Get project folder
project_folder = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------
# STEP 1: OPEN CHROME
# --------------------------------------------------

print("Step 1: Opening Chrome browser...")
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('chrome', interval=0.05)
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

pyautogui.press('tab')
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

# --------------------------------------------------
# STEP 2: OPEN BBC WEATHER
# --------------------------------------------------

pyautogui.hotkey('ctrl', 't')

pyautogui.hotkey('ctrl', 'l')
time.sleep(1)

pyautogui.write(
    'https://www.bbc.com/weather/1264527',
    interval=0.05
)

pyautogui.press('enter')
time.sleep(6)

print("Step 2: BBC weather website opened successfully.")


# --------------------------------------------------
# STEP 3: FIND WEATHER CONTENT
# --------------------------------------------------

print("Step 3: Finding weather information...")

# Open browser Find
pyautogui.hotkey('ctrl', 'f')
time.sleep(1)

# Search for temperature
pyautogui.write('temperature', interval=0.05)
time.sleep(2)

# Close Find box
pyautogui.press('esc')
time.sleep(1)

print("Weather information located.")


# --------------------------------------------------
# STEP 4: SELECT AND COPY PAGE CONTENT
# --------------------------------------------------

print("Step 4: Copying weather data...")

pyautogui.hotkey('ctrl', 'a')
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

print("Weather data copied successfully.")


# --------------------------------------------------
# STEP 5: OPEN EXCEL
# --------------------------------------------------

print("Step 5: Opening Microsoft Excel...")


pyautogui.hotkey('shift', 'ctrl', 'alt', 'win', 'x')
time.sleep(1)

pyautogui.press('enter')
time.sleep(5)

print("Excel opened successfully.")


# --------------------------------------------------
# STEP 6: CREATE NEW WORKBOOK
# --------------------------------------------------

pyautogui.hotkey('ctrl', 'n')
time.sleep(1)
pyautogui.press('enter')

print("New Excel workbook created.")



# --------------------------------------------------
# STEP 7: PASTE WEATHER DATA
# --------------------------------------------------

pyautogui.hotkey('ctrl', 'v')
time.sleep(3)

print("Weather data pasted into Excel.")


# --------------------------------------------------
# STEP 8: SAVE EXCEL FILE
# --------------------------------------------------

# Save the Excel file with today's date


today = datetime.now().strftime("%Y-%m-%d")

filename = f"daily_report_{today}.xlsx"
file_path = os.path.join(project_folder, filename)

# Save Excel file
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

pyautogui.press('tab', presses=3, interval=0.2)
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)


pyautogui.write(file_path, interval=0.03)
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

print("Excel file saved:", file_path)


# Take screenshot of the final Excel sheet
screenshot_name = f"daily_report_{today}.png"
screenshot_path = os.path.join(project_folder, screenshot_name)

pyautogui.screenshot(screenshot_path)

print("Screenshot saved:", screenshot_path)