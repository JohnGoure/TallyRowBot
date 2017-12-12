import pyautogui
import time

pyautogui.PAUSE =.06
pyautogui.FAILSAFE = True

class Player():
    def __init__(self):
        self._move_Right_String = 'right'
        self._move_Left_String = 'left'
        self._up_String = 'up'
        self._down_String = 'down'
        self._jump_String = 'z'
        self._select_String = 'z'
        self._attack_String = 'x'
        self._dash_String = 'c'
        self._super_Dash_String = 's'
        self._focus_Cast_String = 'a'
        self._quick_Map_String = 'b'
        self._dream_Nail_String = 'd'
        self._quick_Cast_String = 'f'
        self._inventory_String = 'i'
        self._quickMapUp = False
        self._superDash_Charging = False
        self._moves_made = []

    def lookUp(self):
        pyautogui.keyDown(self._up_String)
        self._moves_made.append(self._up_String)

    def lookDown(self):
        pyautogui.keyDown(self._down_String)
        self._moves_made.append(self._down_String)

    def holdRight(self):
        pyautogui.keyDown(self._move_Right_String)
        self._moves_made.append(self._move_Right_String)

    def holdLeft(self):
        pyautogui.keyDown(self._move_Left_String)
        self._moves_made.append(self._move_Left_String)

    def stop(self):
        pyautogui.keyUp(self._moves_made.pop())

    def longStepRight(self):
        pyautogui.keyDown(self._move_Right_String)
        time.sleep(.7)
        pyautogui.keyUp(self._move_Right_String)

    def shortStepRight(self):
        pyautogui.press(self._move_Right_String)

    def longStepLeft(self):
        pyautogui.keyDown(self._move_Left_String)
        time.sleep(.7)
        pyautogui.keyUp(self._move_Left_String)

    def shortStepLeft(self):
        pyautogui.press(self._move_Left_String)

    def jump(self):
        pyautogui.keyDown(self._jump_String)
        time.sleep(.17)
        pyautogui.keyUp(self._jump_String)

    def longJump(self):
        pyautogui.keyDown(self._jump_String)

    def dash(self):
        pyautogui.press(self._dash_String)

    def superDash(self):
        if self._superDash_Charging == False:
            pyautogui.keyDown(self._super_Dash_String)
            self._superDash_Charging = True
        else:
            pyautogui.keyUp(self._super_Dash_String)
            self._superDash_Charging = False

    def attack(self):
        pyautogui.press(self._attack_String)

    def upAttack(self):
        pyautogui.keyDown(self._up_String)
        self.attack()
        pyautogui.keyUp(self._up_String)

    def downAttack(self):
        pyautogui.keyDown(self._down_String)
        self.attack()
        pyautogui.keyUp(self._down_String)

    def inventory(self):
        pyautogui.press(self._inventory_String)

    def select(self):
        pyautogui.press(self._select_String)


    def quickMap(self):
        if self._quickMapUp == False:
            pyautogui.keyDown(self._quick_Map_String)
            self._quickMapUp = True
        else:
            pyautogui.keyUp(self._quick_Map_String)
            self._quickMapUp = False

    def quickCast(self):
        pyautogui.press(self._quick_Cast_String)

    def focusCast(self):
        pyautogui.press(self._focus_Cast_String)
