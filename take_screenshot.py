"""Used to take screenshot from a window without requiring focus"""
import cv2
import no_mouse_click
import win32gui, win32ui, win32con
import numpy as np


class PrintScreen:
    def __init__(self, windowname):
        self.windowname = windowname
        self.hwnd = win32gui.FindWindow(None, self.windowname)
        self.x, self.y, self.w, self.h = win32gui.GetWindowRect(win32gui.FindWindow(None, self.windowname))
        self.wDC = win32gui.GetWindowDC(self.hwnd)
        self.dcObj = win32ui.CreateDCFromHandle(self.wDC)
        self.cDC = self.dcObj.CreateCompatibleDC()
        self.dataBitMap = win32ui.CreateBitmap()
        self.dataBitMap.CreateCompatibleBitmap(self.dcObj, self.w-self.x, self.h-self.y)
        self.cDC.SelectObject(self.dataBitMap)
    
    def free_resources(self):
        self.dcObj.DeleteDC()
        self.cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, self.wDC)
        win32gui.DeleteObject(self.dataBitMap.GetHandle())

    def take_screenshot(self, color=True):
        self.cDC.BitBlt((0,0),(self.w-self.x, self.h-self.y) , self.dcObj, (0,0), win32con.SRCCOPY)
        im = self.dataBitMap.GetBitmapBits(True)
        img = np.fromstring(im, dtype='uint8').reshape(self.h-self.y, self.w-self.x, 4)
        if not color:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
        return img, self.x, self.y

if __name__ == "__main__":
    ss = PrintScreen('Selling')
    try:
        count= 1
        while True:
            image, _, _ = ss.take_screenshot()
            # image = take_screenshot('Main Acc')
            # cv2.imshow('img', image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            count+=1
            print(count)
    except KeyboardInterrupt:
        pass
    
    ss.free_resources()
