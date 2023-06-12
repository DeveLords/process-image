import cv2
from PySide6.QtGui import QPixmap, QImage


class image:
    def __init__(self, filePath: str):
        self._image = cv2.imread(filePath)
        self._processedImage = self._image.copy()
        self._width = self._image.shape[0]
        self._height = self._image.shape[1]
        self._filePath = filePath

    def convertCV2toQt(self, cv2Image=None):
        if cv2Image is None:
            rgbImg = cv2.cvtColor(self._image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImg.shape
            bytesPerLine = ch * w
            p = QImage(rgbImg.data, w, h, bytesPerLine, QImage.Format_RGB888)
            p = QPixmap.fromImage(p)
            return p
        else:
            rgbImg = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImg.shape
            bytesPerLine = ch * w
            p = QImage(rgbImg.data, w, h, bytesPerLine, QImage.Format_RGB888)
            p = QPixmap.fromImage(p)
            return p

    def getFilePath(self):
        return self._filePath

    def getImage(self):
        return self._image

    def getFileName(self):
        index = self._filePath.rfind('\\')
        fileName = self._filePath[index + 1:]
        return fileName

    def getWidthImage(self):
        return self._width

    def getHeightImage(self):
        return self._height

    def getSizeImage(self):
        return self._width, self._height
