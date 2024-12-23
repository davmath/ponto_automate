import pyautogui
from time import sleep

pyautogui.PAUSE = 1

def vpn_process():
    
    pyautogui.hotkey('win')
    pyautogui.write('forticlient')
    pyautogui.hotkey('enter')
    sleep(3)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    sleep(15)
    pyautogui.hotkey('alt', 'f4')

