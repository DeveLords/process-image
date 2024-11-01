from infraImage import infraImage
from visibleImage import visibleImage

class imageContainer:
    def __init__(self, filesList = None, dirPath = None):
        self.imageList = []
        for i, values in enumerate(filesList):
            self.imageList.append((infraImage(dirPath + '/infra/' + values[0],
                                            values[1], values[2]),
                                       visibleImage(dirPath + '/visible/' + values[0])))

    def getListImages(self):
        fileList = []
        for i in self.imageList:
            fileList.append(i[0].getFileName())
        return fileList

    def getImageForDisplaying(self, index, typeImage):
        concrateImage = self.imageList[index]

        image = concrateImage[typeImage].convertCV2toQt()

        imageName = concrateImage[0].getFileName()
        tempMin = concrateImage[0].getTempMin()
        tempMax = concrateImage[0].getTempMax()
        return (image, imageName, tempMin, tempMax)

    def processImage(self, index, typeProcess, tempMin = None, tempMax = None):
        concrateImage = self.imageList[index]
        match typeProcess:
            case 1:
                processedImage = concrateImage[0].convertCV2toQt()
            case 2:
                processedImage = concrateImage[0].getAreaHot()
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
            case 3:
                processedImage = concrateImage[0].getAreaCold()
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
            case 4:
                processedImage = concrateImage[0].getAreaAvg()
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
            case 5:
                processedImage = concrateImage[0].getNewColorMap(tempMin, tempMax)
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
            case 6:
                processedImage = concrateImage[0].drawHotPoint()
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
            case 7:
                processedImage = concrateImage[0].drawColdPoint()
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
            case 8:
                processedImage = concrateImage[0].drawAvgPoint()
                processedImage = concrateImage[0].convertCV2toQt(processedImage)
        return processedImage


    def changeColorMap(self, index, tempMin, tempMax):
        concrateImage = self.imageList[index]
        processedImage = concrateImage[0].getNewColorMap(tempMin, tempMax)
        processedImage = concrateImage[0].convertCV2toQt(processedImage)
        return processedImage
