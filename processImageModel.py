from PySide6 import QtCore

from imageContainer import imageContainer

class processImageModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, pathList = None, **kwargs):
        super(processImageModel, self).__init__(*args, **kwargs)
        self.imageContainer = None
        self.imageInf = [['', '', '']]
    
    def setImageContainer(self, imageContainer: imageContainer):
        self.imageContainer = imageContainer
    
    def rowCount(self, index):
        return len(self.imageInf)
    
    def columnCount(self, index):
        return 3
    
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            file = self.imageInf[index.row()][index.column()]
            
            return file
    
    def ProcessImage(self, index, typeDisplay, tempMin = None, tempMax = None):
        return self.imageContainer.processImage(index, typeDisplay, tempMin, tempMax)
    
    def showSelectedImage(self, index, isInafra):
        typeImage = 0 if isInafra is True else 1
        image, imageName, tempMin, tempMax = self.imageContainer.getImageForDisplaying(index, typeImage)
        self.imageInf[0] = [imageName ,tempMin, tempMax]
        return image
    
    def countImage(self):
        return len(self.imageContainer.imageList)
    
    def clearData(self):
        self.imageInf = [['', '', '']]
        self.imageContainer = None
        