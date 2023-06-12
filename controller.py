import csv
from os import listdir, stat
from os.path import isfile, join

class controller:
    def __init__(self) -> None:
        pass
    
    def getAvailableImage(self, dirPath):
        self.dirPath = dirPath
        self.availalbeFiles = [(file, (join(self.dirPath, file))) 
                               for file in listdir(self.dirPath) if 
                               isfile(join(self.dirPath, file))]
        print(self.availalbeFiles)
        return self.availalbeFiles
    
    def saveImages(self):
        pass
    
    def getFileImage(self, indexes):
        fileList = []
        for index in indexes:
            with open(self.availalbeFiles[index][1], encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=';')
                next(file_reader)
                for raw in file_reader:
                    fileName = raw[0][-12:].replace('IS2', 'bmp')
                    coldPoint = float(raw[4].replace(',', '.'))
                    hotpoint = float(raw[5].replace(',', '.'))
                    fileList.append((fileName, coldPoint, hotpoint))
        return fileList, self.dirPath
