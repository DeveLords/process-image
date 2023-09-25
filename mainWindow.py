
from PySide6.QtWidgets import (QFileDialog, 
                               QMainWindow,
                               QWidget,  
                               QLabel, 
                               QToolBar,
                               QHBoxLayout,
                               QListView,
                               QSizePolicy)
from processImageWidget import processImageWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from getImageWindow import getImageWindow
from modelListImage import modelListImage
from infraImage import *
from visibleImage import *
import os

CUREENT_DIR = os.getcwd()
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)
        self.setWindowTitle('Обработчик изображений')
        
    def init_ui(self):
        
        self.icoDir = CUREENT_DIR + '\icons\ico\\'
        self._createMenuBar()
        self._createToolBar()
        self.createCentralArea()
        self.statusBar().showMessage("Готово к работе")

    def _createToolBar(self):
        toolBar = QToolBar('Файл')
        openAction = QAction(QIcon(self.icoDir + '32x32\\open.ico'), "Открыть", self)
        saveAction = QAction(QIcon(self.icoDir + '32x32\\save.ico'), "Сохранить", self)
        closeAction = QAction(QIcon(self.icoDir + '32x32\\exit.ico'), "Закрыть", self)
        openAction.setToolTip('Загрузить изображения')
        saveAction.setToolTip('Сохранить изображения')
        closeAction.setToolTip('Закрыть изображения')

        toolBar.addAction(openAction)
        toolBar.addAction(saveAction)
        toolBar.addAction(closeAction)
        self.addToolBar(toolBar)
        toolBar.show()

        closeAction.triggered.connect(self.closeWorkplace)
        openAction.triggered.connect(self.OpenFileImage)

    def _createMenuBar(self):
        self.getImageWindow = getImageWindow()

        openAction = QAction(QIcon(self.icoDir + '16x16\\open.ico'),'Загрузить', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Загрузить набор изображений')
        
        saveAction = QAction(QIcon(self.icoDir + '16x16\\save.ico'),'Загрузить', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Сохранить набор изображений')

        closeAction = QAction(QIcon(self.icoDir + '16x16\\exit.ico'), 'Закрыть', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Закрыть')
        closeAction.triggered.connect(self.closeWorkplace)

        exitAction = QAction(QIcon(self.icoDir + '16x16\\delete.ico'), 'Выход', self)
        exitAction.setShortcut('Esc')
        exitAction.setStatusTip('Выйти из программы')
        exitAction.triggered.connect(self.close)

        aboutAction = QAction(text='О программе', parent=self)
        aboutAction.setStatusTip('Информация о текущей версии программы')

        helpAction = QAction(text='Помощь', parent=self)
        helpAction.setStatusTip('Помощь по программе')

        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('Файл')
        helpMenu = menuBar.addMenu('Справка')

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(closeAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        helpMenu.addAction(aboutAction)
        helpMenu.addAction(helpAction)

        openAction.triggered.connect(self.OpenFileImage)
    
    def createCentralArea(self):
        self.listViewImages = QListView()
        self.modelListImage = modelListImage()
        self.listViewImages.setModel(self.modelListImage)
        
        self.processImageView = processImageWidget()
        self.listViewImages.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        centrWidget = QWidget()
        
        centralAreaLayout = QHBoxLayout()
        centralAreaLayout.addWidget(self.listViewImages)
        centralAreaLayout.addWidget(self.processImageView)
        
        centrWidget.setLayout(centralAreaLayout)
        
        self.setCentralWidget(centrWidget)
    
    def OpenFileImage(self):
        self.getImageWindow.openFiles()
        imageContainer = self.getImageWindow.getImageContainerFromModel()
        self.processImageView.setImageContainerModel(imageContainer)
        self.modelListImage.showListImage(imageContainer)
        self.modelListImage.layoutChanged.emit()
        
        self.listViewImages.selectionModel().currentChanged.connect(self.on_row_changed)
        
    def on_row_changed(self, current, previous):
        self.processImageView.showSelectedImage(current.row())
        
    def saveWorkArea(self):
        QFileDialog.getSaveFileName(self)

    def closeWorkplace(self):
        self.processImageView.clearArea()
        self.modelListImage.clearData()
        self.modelListImage.layoutChanged.emit()