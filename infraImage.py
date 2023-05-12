# Наследуемый класс для инфракрасного изображения
# наследуемый от класса image

from image import image
import numpy as np

class infraImage(image):
    def __init__(self, filePath: str, temperatureMin, temperatureMax, cmap=None, tempMap= None) -> None:
        super().__init__(filePath)
        self.tempMin = temperatureMin
        self.tempMax = temperatureMax

    def getTempMin(self):
        return self.tempMin

    def getTempMax(self):
        return self.tempMax
    # Паблик методы, которые будут испльзоваться для решения различных задач
    # Методы для выделения горячих/холодных областей
    def getAreaCold(self):
        img = self._image.copy
        matrixSum = self._createSumBGR()
        mean = self._findMean(matrixSum)
        meanArea = self._findMean(matrixSum, mean, '<')
        for i in range(len(matrixSum)):
            for j in range(len(matrixSum[i])):
                if matrixSum[i][j] > meanArea:
                    img[i][j] = [0, 0, 0]
        return img

    def getAreaHot(self):
        img = self._image.copy
        matrixSum = self._createSumBGR()
        mean = self._findMean(matrixSum)
        meanArea = self._findMean(matrixSum, mean, '>')
        for i in range(len(matrixSum)):
            for j in range(len(matrixSum[i])):
                if matrixSum[i][j] < meanArea:
                    img[i][j] = [0, 0, 0]
        return img

    def getAreaAvg(self):
        img = self._image.copy
        matrixSum = self._createSumBGR()
        mean = self._findMean(matrixSum)
        for i in range(len(matrixSum)):
            for j in range(len(matrixSum[i])):
                if (matrixSum[i][j] < mean) or (matrixSum[i][j] > mean):
                    img[i][j] = [0, 0, 0]
        return img

    # Блок методов для получения цветовой карты
    def getTempMap(self):
        return self._createTempMap(self.tempMin, self.tempMax)

    def getNewColorMap(self, tMin, tMax):
        tempMap = self._createTempMap(self.tempMin, self.tempMax)
        return self._createColorMap(tempMap, tMin, tMax)

    # Метод наложения маски
    def overlayMask(self):
        pass

    def _rgbToTemperature(self, rg, tMin, tMax):
        if isinstance(rg, tuple) or isinstance(rg, list):
            temp = tMin + (rg[-1] + rg[-2])/510 * (tMax - tMin)
        else:
            temp = tMin + (rg / 510) * (tMax - tMin)
        return temp

    def _tempToBGR(self, temperature, tmin, tmax):
        r = 0
        g = 0
        gr = 510*(temperature - tmin)/(tmax-tmin)
        if gr > 255:
            r = 255
            r = gr - 255
        elif gr >= 0:
            g = 0
            r = gr
        else:
            return g, r
        return g, r

    def _createTempMap(self, tMin, tMax):
        tempMatrix = np.zeros((self._width, self._height))
        for i in range(self._width):
            for j in range(self._height):
                sumBGR = infraImage[i][j].sum()
                tempMatrix[i][j] = self._rgbToTemperature(sumBGR, tMin, tMax)
        return tempMatrix

    def _createColorMap(self, tempMatrix, tMin, tMax):
        image = np.zeros((self._width, self._height, 3), dtype=np.uint16)
        for i in range(self._width):
            for j in range(self._height):
                G, R = self.tempToBGR(tempMatrix[i][j], tMin, tMax)
                BGR = np.array([0, G, R])
                image[i][j] = BGR
        return image

    # Блок методов для расчета зон
    def _createSumBGR(self):
        sumBGR = np.zeros((self._width, self._height), dtype=np.uint16)
        for i in range(self._width):
            for j in range(self._height):
                sumBGR[i][j] = self._image[i][j].sum()
        return sumBGR

    def _findMean(self, matrixSum, matrixMean=None, oper=None):
        summa = 0
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
