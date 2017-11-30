import pyautogui
import time

point = pyautogui.locateCenterOnScreen('image/5.png')
pyautogui.click(point[0],point[1])

point = pyautogui.locateCenterOnScreen('image/x.png')
pyautogui.click(point[0],point[1])

point = pyautogui.locateCenterOnScreen('image/9.png')
pyautogui.click(point[0],point[1])

point = pyautogui.locateCenterOnScreen('image/=.png')
pyautogui.click(point[0],point[1])
