import cv2
from cameo2.managers import WindowManager, CaptureManager

class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager("Cameo", self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                pass
            self._captureManager.exitFrame()
            self._windowManager.processEvent()

    def onKeypress(self, keycode):
        if keycode == 32: #space
            self._captureManager.writeImage("screenShot.png")
        elif keycode == 9:  #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo("screencast.avi")
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: #escape
            self._windowManager.destroyWindow()




if __name__ == "__main__":
    Cameo().run()