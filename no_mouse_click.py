'''SEND CLICKS WITHOUT MOVING THE MOUSE'''
import win32con
from win32api import MAKELONG, SendMessage
from win32gui import FindWindow

RIGHT_BTN_STATE = win32con.MK_RBUTTON
HOLD_RIGHT_BTN = win32con.WM_RBUTTONDOWN
RELEASE_RIGHT_BTN = win32con.WM_RBUTTONUP
LEFT_BTN_STATE = win32con.MK_LBUTTON
HOLD_LEFT_BTN = win32con.WM_LBUTTONDOWN
RELEASE_LEFT_BTN = win32con.WM_LBUTTONUP
MIDDLE_BTN_STATE = win32con.MK_MBUTTON
HOLD_MIDDLE_BTN = win32con.WM_MBUTTONDOWN
RELEASE_MIDDLE_BTN = win32con.WM_MBUTTONUP

BUTTONS = {
    "left": [LEFT_BTN_STATE, HOLD_LEFT_BTN, RELEASE_LEFT_BTN],
    "right": [RIGHT_BTN_STATE, HOLD_RIGHT_BTN, RELEASE_RIGHT_BTN],
    "middle": [MIDDLE_BTN_STATE, HOLD_MIDDLE_BTN, RELEASE_MIDDLE_BTN]
}


def click(window_name, button: str, coords: tuple):
    window = FindWindow(None, window_name)
    coords = MAKELONG(coords[0], coords[1])
    try:
        state, hold, release = BUTTONS[button]
    except KeyError:
        raise Exception('Argument invalid, correct ones are: left, right, middle')
    SendMessage(window, hold, state, coords)
    SendMessage(window, release, 0, coords)
