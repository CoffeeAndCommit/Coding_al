import pyautogui
import time

print("Teams activity script is running. Press Ctrl+C to stop.")

while True:
    x, y = pyautogui.position()

    pyautogui.moveTo(x + 1, y, duration=0.1)
    pyautogui.moveTo(x, y, duration=0.1)

    time.sleep(30)