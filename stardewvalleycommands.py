import pyautogui

pyautogui.PAUSE =.159
pyautogui.FAILSAFE = True

class StardewValleyCommands():
    """ This class implements the model for Stardew Valley Commands"""
    # initialize the class with the strings associated with the keyboard commands
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

    def moveup(self):
        pyautogui.keyDown(self._up)
        pyautogui.keyUp(self._up)
        print("Keyboard pressed: " + self._up)

    def movedown(self):
        pyautogui.keyDown(self._down)
        pyautogui.keyUp(self._down)
        print("Keyboard pressed: " + self._down)

    def moveleft(self):
        pyautogui.keyDown(self._left)
        pyautogui.keyUp(self._left)
        print("Keyboard pressed: " + self._left)

    def moveright(self):
        pyautogui.keyDown(self._right)
        pyautogui.keyUp(self._right)
        print("Keyboard pressed: " + self._right)

    def openmap(self):
        pyautogui.keyDown(self._map)
        pyautogui.keyUp(self._map)
        print("Keyboard pressed: " + self._map)

    def openmenu(self):
        pyautogui.keyDown(self._menu)
        pyautogui.keyUp(self._menu)
        print("Keyboard pressed: " + self._menu)

    def openjournal(self):
        pyautogui.keyDown(self._journal)
        pyautogui.keyUp(self._journal)
        print("Keyboard pressed: " + self._journal)

    def leftclick(self):
        pyautogui.keyDown(self._leftclick)
        pyautogui.keyUp(self._leftclick)
        print("Keyboard pressed: " + self._leftclick)

    def rightclick(self):
        pyautogui.keyDown(self._rightclick)
        pyautogui.keyUp(self._rightclick)
        print("Keyboard pressed: " + self._rightclick)

    def escape(self):
        pyautogui.keyDown(self._esc)
        pyautogui.keyUp(self._esc)
        print("Keyboard pressed: " + self._esc)


player = StardewValleyCommands()

player.openmenu()
