'''This is used to drag (scroll) the screen in android emualators on windows
without using the mouse and without window focus.
Only tested on NOX'''
from win32api import MAKELONG, SendMessage, PostMessage
from win32gui import FindWindow
from time import sleep

def drag(window_name: str, coords: tuple, to_y: int):
    """Window_name: The name of the emulator window without the version
    coords: mouse cordinates from where the scroll should start (x, y)
    to_y: maximum y range that scroll should stop."""
    x, y = coords
    window = FindWindow(None, window_name)
    coords = MAKELONG(coords[0], coords[1])
    SendMessage(window, 0x201, 0x0001, coords)
    
    while y < to_y:
        y+=1
        coords = MAKELONG(x, y)
        SendMessage(window, 0x200, 0x0001, coords) 
        sleep(0.001)
    SendMessage(window, 0x202, 0, coords)