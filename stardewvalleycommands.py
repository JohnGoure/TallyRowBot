import pyautogui

#slow down the keyboard inputs, so that Stardew Valley receives the input.
pyautogui.PAUSE =.159

# FAILSAFE allows the host to turn off pyauotgui
# by moving the mouse to the top left of the monitor very quickly
pyautogui.FAILSAFE = True

""" This class implements the model for Stardew Valley Commands
    initialize the class with the strings associated with the keyboard commands"""
class StardewValleyCommands():

    def __init__(self):
        self._up = 'w'
        self._down = 's'
        self._left = 'a'
        self._right = 'd'
        self._map = 'm'
        self._menu = 'e'
        self._journal = 'f'
        self._leftclick = 'c'
        self._rightclick = 'x'
        self._esc = 'esc'
        self._one = '1'
        self._two = '2'
        self._three = '3'
        self._four = '4'
        self._five = '5'
        self._six ='6'
        self._seven = '7'
        self._eight = '8'
        self._nine = '9'
        self._zero = '0'
        self._minus = '-'
        self._equals = '='

    """ Stardew Valley Commands """
    def moveup(self):
        pyautogui.keyDown(self._up)
        pyautogui.keyUp(self._up)

    def movedown(self):
        pyautogui.keyDown(self._down)
        pyautogui.keyUp(self._down)

    def moveleft(self):
        pyautogui.keyDown(self._left)
        pyautogui.keyUp(self._left)

    def moveright(self):
        pyautogui.keyDown(self._right)
        pyautogui.keyUp(self._right)

    def openmap(self):
        pyautogui.keyDown(self._map)
        pyautogui.keyUp(self._map)

    def openmenu(self):
        pyautogui.keyDown(self._menu)
        pyautogui.keyUp(self._menu)

    def openjournal(self):
        pyautogui.keyDown(self._journal)
        pyautogui.keyUp(self._journal)

    def leftclick(self):
        pyautogui.click()

    def rightclick(self):
        pyautogui.keyDown(self._rightclick)
        pyautogui.keyUp(self._rightclick)

    def escape(self):
        pyautogui.keyDown(self._esc)
        pyautogui.keyUp(self._esc)

    def tool_1(self):
        pyautogui.keyDown(self._one)
        pyautogui.keyUp(self._one)

    def tool_2(self):
        pyautogui.keyDown(self._two)
        pyautogui.keyUp(self._two)

    def tool_3(self):
        pyautogui.keyDown(self._three)
        pyautogui.keyUp(self._three)

    def tool_4(self):
        pyautogui.keyDown(self._four)
        pyautogui.keyUp(self._four)

    def tool_5(self):
        pyautogui.keyDown(self._five)
        pyautogui.keyUp(self._five)

    def tool_6(self):
        pyautogui.keyDown(self._six)
        pyautogui.keyUp(self._six)

    def tool_7(self):
        pyautogui.keyDown(self._seven)
        pyautogui.keyUp(self._seven)

    def tool_8(self):
        pyautogui.keyDown(self._eight)
        pyautogui.keyUp(self._eight)

    def tool_9(self):
        pyautogui.keyDown(self._nine)
        pyautogui.keyUp(self._nine)

    def tool_10(self):
        pyautogui.keyDown(self._zero)
        pyautogui.keyUp(self._zero)

    def tool_11(self):
        pyautogui.keyDown(self._minus)
        pyautogui.keyUp(self._minus)

    def tool_12(self):
        pyautogui.keyDown(self._equals)
        pyautogui.keyUp(self._equals)
