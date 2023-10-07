import pyautogui
import time 

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

print("width: " + str(screenWidth) + " height: " + str(screenHeight))

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print("x: " + str(currentMouseX) + " y: " + str(currentMouseY))

for x in range(15):
  pyautogui.moveRel(10, 0)
  time.sleep(.1)

pyautogui.click()
