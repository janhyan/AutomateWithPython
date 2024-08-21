import subprocess
import pyautogui

subprocess.call('D:\Program Files\Oracle\VirtualBox')

def clickVM():
    pyautogui.moveTo(1498, 70)

    if pyautogui.pixel(1498, 70)[0] > 150:
        pyautogui.click()