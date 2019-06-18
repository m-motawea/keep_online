import pyautogui
import time
import ctypes
user32 = ctypes.windll.User32

def isLocked():
    return user32.GetForegroundWindow() == 0

screenWidth, screenHeight = pyautogui.size()
initialMouseX, initialMouseY = pyautogui.position()


print("screenWidth: {}, screenHeight: {}".format(screenWidth, screenHeight))
print("currentX: {}, currentY: {}".format(initialMouseX, initialMouseY))

step = 2
FLAG = True
pre_x = None
pre_y = None
period = 60

while True:
    if not isLocked():
        if FLAG:
            print("not locked. moving mouse")
            pyautogui.moveTo(screenWidth/step, screenHeight/step)
            time.sleep(period)
        else:
            time.sleep(period)

        currentMouseX, currentMouseY = pyautogui.position()


        if currentMouseX != screenWidth/step or currentMouseY != screenHeight/step:
            if pre_x and pre_y:
                if pre_x == currentMouseX and pre_y == currentMouseY:
                    FLAG = True
                    continue

            pre_x = currentMouseX
            pre_y = currentMouseY
            print("mouse moved")
            FLAG = False
        else:
            FLAG = True
            if step == 2:
                step = 4
            else:
                step = 2
    else:
        print("locked")
