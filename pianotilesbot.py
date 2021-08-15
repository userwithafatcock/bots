from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile 1 position X: 1450 Y: 450 
#tile 2 position X: 1512 Y: 450
#tile 3 position X: 1600 Y: 450
#tile 4 position X: 1679 Y: 450

time.sleep(3) #wait 3 seconds until bot starts

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep (0.01) #pause after click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(1450, 450)[0] == 0:
        click(1450,450)
    if pyautogui.pixel(1512, 450)[0] == 0:
        click(1512,450)
    if pyautogui.pixel(1600, 450)[0] == 0:
        click(1600,450)
    if pyautogui.pixel(1679, 450)[0] == 0:
        click(1679,450)
   
        
