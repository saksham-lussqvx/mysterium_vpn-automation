# NOTE: Make sure that VPN is in full screen mode and isn't minimized
import pyautogui
import time
import win32gui, win32com.client

class mysterium:
    # set a simple true and false for pattern matching
    def __init__(self, country="", match=True, max_tries=3):
        self.match = match
        self.max_tries = max_tries
        self.country = country

    def connect(self):
        while self.max_tries > 0:
            # find the window and bring it to the front
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            hwnd = win32gui.FindWindow(None, 'Mysterium VPN')
            win32gui.ShowWindow(hwnd,5)
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(2)
            element = pyautogui.locateCenterOnScreen('temp_1.png')
            pyautogui.click(element)
            time.sleep(1)
            # triple click on the text
            for i in range(3):
                pyautogui.click(element)
            pyautogui.press('backspace')
            time.sleep(0.5)
            pyautogui.typewrite(country)
            time.sleep(3)
            # click on the first option
            element_2 = pyautogui.locateCenterOnScreen('temp_2.png')
            print(element_2)
            pyautogui.click(element_2)
            time.sleep(7)
            if self.max_tries > 0:
                self.max_tries -= 1
            if self.match == True:
                if pyautogui.locateCenterOnScreen('temp_3.png') != None:
                    return True
            else:
                return True
        return False

    
    def disconnect(self):
        hwnd = win32gui.FindWindow(None, 'Mysterium VPN')
        win32gui.ShowWindow(hwnd, 5)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(2)
        element = pyautogui.locateCenterOnScreen('temp_3.png')
        pyautogui.click(element)
