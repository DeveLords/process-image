from PySide6 import QtWidgets, QtGui, QtCore
from getImageModel import getImageModel

class getImageWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Загрузка изображений")

        self.listFiles = QtWidgets.QListView()
        self.getImageView = getImageModel()
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        self.listFiles.setModel(self.getImageView)
        self.listFiles.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)

        mainGetImageLayout = QtWidgets.QVBoxLayout()

        loadButton = QtWidgets.QPushButton("Загрузить выбранные")
        closeButton = QtWidgets.QPushButton("Закрыть без загрузки")
        selectAllButton = QtWidgets.QPushButton("Выбрать все")
        clearSelectAllButton = QtWidgets.QPushButton("Снять выделение")

        loadButton.pressed.connect(self.getIndex)
        selectAllButton.pressed.connect(self.selectAllElem)
        clearSelectAllButton.pressed.connect(self.clearSelectionAllElem)
        closeButton.pressed.connect(self.hide)

        mainGetImageLayout.addWidget(self.listFiles)
        mainGetImageLayout.addWidget(loadButton)
        mainGetImageLayout.addWidget(selectAllButton)
        mainGetImageLayout.addWidget(clearSelectAllButton)
        mainGetImageLayout.addWidget(closeButton)

        self.setLayout(mainGetImageLayout)

    def openFiles(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                          'Выберите папку:',
                                                          '/home/gamkere/Code/process-image',
                                                          QtWidgets.QFileDialog.ShowDirsOnly)
        self.getImageView.getListImage(dir_)

        self.exec()

        self.getImageView.layoutChanged.emit()

    def getIndex(self):
        indexes = self.listFiles.selectionModel().selectedIndexes()
        indexes = [i.row() for i in indexes]
        indexes.sort()
        self.hide()
        self.getImageView.getAllocatedImage(indexes)

    def getImageContainerFromModel(self):
        return self.getImageView.getImageContainer()

    def selectAllElem(self):
        self.listFiles.selectAll()
        self.getImageView.layoutChanged.emit()

    def clearSelectionAllElem(self):
        self.listFiles.clearSelection()
        self.getImageView.layoutChanged.emit()

