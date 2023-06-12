from image import image
import numpy as np
import cv2 as cv

class infraImage(image):
    def __init__(self, filePath: str, temperatureMin, temperatureMax, cmap=None, tempMap= None) -> None:
        super().__init__(filePath)
        self.tempMin = temperatureMin
        self.tempMax = temperatureMax

    def getTempMin(self):
        return self.tempMin

    def getTempMax(self):
        return self.tempMax
    
    def getAreaCold(self):
        img = self._image.copy()
        matrixSum = self._createSumBGR()
        mean = self._findMean(matrixSum)
        meanArea = self._findMean(matrixSum, mean, '<')
        for i in range(len(matrixSum)):
            for j in range(len(matrixSum[i])):
                if matrixSum[i][j] > meanArea:
                    img[i][j] = [0, 0, 0]
        return img

    def getAreaHot(self):
        img = self._image.copy()
        matrixSum = self._createSumBGR()
        mean = self._findMean(matrixSum)
        meanArea = self._findMean(matrixSum, mean, '>')
        for i in range(len(matrixSum)):
            for j in range(len(matrixSum[i])):
                if matrixSum[i][j] < meanArea:
                    img[i][j] = [0, 0, 0]
        return img

    def getAreaAvg(self):
        img = self._image.copy()
        matrixSum = self._createSumBGR()
        mean = self._findMean(matrixSum)
        meanAreaHot = self._findMean(matrixSum, mean, '>')
        meanAreaCold = self._findMean(matrixSum, mean, '<')
        for i in range(len(matrixSum)):
            for j in range(len(matrixSum[i])):
                if (matrixSum[i][j] > meanAreaHot) or (matrixSum[i][j] < meanAreaCold):
                    img[i][j] = [0, 0, 0]
        return img

    def getTempMap(self):
        return self._createTempMap(self.tempMin, self.tempMax)

    def getNewColorMap(self, tMin, tMax):
        tempMap = self._createTempMap(self.tempMin, self.tempMax)
        return self._createColorMap(tempMap, tMin, tMax)

    def _rgbToTemperature(self, rg, tMin, tMax):
        temp = tMin + (rg / 510) * (tMax - tMin)
        return temp
    
    def drawHotPoint(self):
        imageDot = self._image.copy()
        tempMap = self._createTempMap(self.tempMin, self.tempMax)
        hotPoint = np.unravel_index(tempMap.argmax(), tempMap.shape)
        image = cv.circle(imageDot, hotPoint, 1, (255, 0, 0), 4)
        return image

    def drawColdPoint(self):
        imageDot = self._image.copy()
        tempMap = self._createTempMap(self.tempMin, self.tempMax)
        hotPoint = np.unravel_index(tempMap.argmin(), tempMap.shape)
        image = cv.circle(imageDot, hotPoint, 1, (255, 0, 0), 4)
        return image
    
    def _tempToBGR(self, temperature, tmin, tmax):
        r = 0
        g = 0
        gr = 510*(temperature - tmin)/(tmax-tmin)
        if gr > 255:
            r = 255
            g = gr - 255
            if g > 255:
                g = 255
            else:
                g = int(g)
        elif gr >= 0:
            g = 0
            r = int(gr)
        else:
            return g, r
        return g, r

    def _createTempMap(self, tMin, tMax):
        tempMatrix = np.zeros((self._width, self._height))
        for i in range(self._width):
            for j in range(self._height):
                sumBGR = self._image[i][j].sum()
                tempMatrix[i][j] = self._rgbToTemperature(sumBGR, tMin, tMax)
        return tempMatrix

    def _createColorMap(self, tempMatrix, tMin, tMax):
        image = self._image.copy()
        for i in range(self._width):
            for j in range(self._height):
                G, R = self._tempToBGR(tempMatrix[i][j], tMin, tMax)
                image[i][j] = [0, G, R]
        return image

    def _createSumBGR(self):
        sumBGR = np.zeros((self._width, self._height), dtype=np.uint16)
        for i in range(self._width):
            for j in range(self._height):
                sumBGR[i][j] = self._image[i][j].sum()
        return sumBGR

    def _findMean(self, matrixSum, matrixMean=None, oper=None):
        summa = 0
        lenght = 0
        if matrixMean is None:
            for i in range(len(matrixSum)):
                for j in range(len(matrixSum[i])):
                    if matrixSum[i][j]:
                        summa += matrixSum[i][j]
                        lenght += 1
        elif oper == '>' or oper is None:
            for i in range(len(matrixSum)):
                for j in range(len(matrixSum[i])):
                    if matrixSum[i][j] > matrixMean:
                        summa += matrixSum[i][j]
                        lenght += 1
        elif oper == '<':
            for i in range(len(matrixSum)):
                for j in range(len(matrixSum[i])):
                    if matrixSum[i][j] != 0 and matrixSum[i][j] < matrixMean:
                        summa += matrixSum[i][j]
                        lenght += 1
        mean = summa / lenght
        return mean
