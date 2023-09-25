from imageContainer import imageContainer
from PySide6 import QtCore

class modelListImage(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(modelListImage, self).__init__(*args, **kwargs)
        self.imageContainer = None
        self.listImage = []
    
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            file = self.listImage[index.row()]
            
            return file
            
    def showListImage(self, imageContainer: imageContainer):
        self.imageContainer = imageContainer
        self.listImage = self.imageContainer.getListImages()
        
    def rowCount(self, index):
        return len(self.listImage)
    
    def clearData(self):
        self.imageContainer = None
        self.listImage = []