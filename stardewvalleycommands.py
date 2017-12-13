import pyautogui

#slow down the keyboard inputs, so that Stardew Valley receives the input.
pyautogui.PAUSE =.159

# FAILSAFE allows the host to turn off pyauotgui
# by moving the mouse to the top left of the monitor very quickly
pyautogui.FAILSAFE = True

""" This class implements the model for Stardew Valley Commands
    it also declares and intializes the class with the strings associated with the keyboard commands"""
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
        pyautogui.keyDown(self._leftclick)
        pyautogui.keyUp(self._leftclick)

    def rightclick(self):
        pyautogui.keyDown(self._rightclick)
        pyautogui.keyUp(self._rightclick)

    def escape(self):
        pyautogui.keyDown(self._esc)
        pyautogui.keyUp(self._esc)
