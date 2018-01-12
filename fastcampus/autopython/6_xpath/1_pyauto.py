import pyautogui

width,height = pyautogui.size()
print(width,height)

pyautogui.moveTo(width/2,height/2)

pyautogui.moveRel(100,None)

pyautogui.moveTo(0,height/2)

pyautogui.typewrite('keyboard test')

pyautogui.press('enter')

point = pyautogui.locateCenterOnScreen('image/a.png')

if point:
    pyautogui.click(point[0],point[1])

else:
    print("Couldn't find the target")
