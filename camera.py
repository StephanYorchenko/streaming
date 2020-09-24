from time import time
import pyautogui


class Camera(object):
    def __init__(self):
        self.frames = [] # [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        self.get_screen()
        return open("static/screenshot.png", 'rb').read()

    def get_screen(self):
        try:
            pyautogui.screenshot("static/screenshot.png")
        except OSError:
            pass
