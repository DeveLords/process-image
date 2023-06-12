from PySide6 import QtCore

from controller import controller
from imageContainer import imageContainer

class getImageModel(QtCore.QAbstractListModel):
    def __init__(self, *args, pathList = None, **kwargs):
        super(getImageModel, self).__init__(*args, **kwargs)
        self.pathList = pathList or None
        self.fileList = []
        self.controller = controller()
        self.imageContainer = None
    
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            file, _ = self.fileList[index.row()]
            
            return file
            
    def rowCount(self, index):
        return len(self.fileList)
    
        
    def loadListFile(self):
        pass
    
    def getAllocatedImage(self, indexesImage: list):
        fileList, dirPath = self.controller.getFileImage(indexesImage)
        print(fileList)
        self.imageContainer = imageContainer(fileList, dirPath)
        print(self.imageContainer.getListImages())
        
    def loadAllocatedImage(self):
        pass
    
    def getListImage(self, pathList):
        self.pathList = pathList
        self.fileList =  self.controller.getAvailableImage(self.pathList)
        
    def getImageContainer(self):
        return self.imageContainer