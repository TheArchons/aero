import pyautogui
import time
PLAY_BUTTON = (167, 666)
FREE_FLIGHT = (352, 671)
END_FLIGHT = (868, 1090)
UP_TIME = 240 # time for the airship to go up in seconds
DOWN_TIME = 350 # time for the airship to go down in seconds

GET_POSITION = False

if GET_POSITION:
    while True:
        print(pyautogui.position())

def timedHold(key, t):
    startTime = time.time()
    pyautogui.keyDown(key)
    while ((time.time() - startTime) < t):
        time.sleep(1)
    
    pyautogui.keyUp(key)

flightCounter = 0
while True:
    # get into free flight
    pyautogui.moveTo(PLAY_BUTTON[0], PLAY_BUTTON[1])
    time.sleep(1)
    pyautogui.moveTo(FREE_FLIGHT[0], FREE_FLIGHT[1])
    time.sleep(1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    time.sleep(10) # loading screen
    pyautogui.press('e')
    time.sleep(20) # wait for engine startup

    for _ in range(10): # repeat a few times before resetting
        timedHold('r', UP_TIME)
        timedHold('f', DOWN_TIME)

    # end flight
    pyautogui.moveTo(END_FLIGHT[0], END_FLIGHT[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
