from PySide6.QtWidgets import QFileDialog ,QMainWindow, QMdiArea, QMdiSubWindow, QLabel, QToolBar
from centralWidget import centralWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from csvReading import csvReading
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
        self.setWindowTitle('Инфракрасные изображения')

    def init_ui(self):
        self.icoDir = CUREENT_DIR + '\icons\ico\\'
        self._createMenuBar()
        self._createToolBar()

    def _createToolBar(self):
        toolBar = QToolBar('Файл')
        openAction = QAction(QIcon(self.icoDir + '32x32\\open.ico'), "Открыть", self)
        saveAction = QAction(QIcon(self.icoDir + '32x32\\save.ico'), "Сохранить", self)
        saveActionAs = QAction(QIcon(self.icoDir + '32x32\\save as.ico'), "Сохранить как...", self)
        closeAction = QAction(QIcon(self.icoDir + '32x32\\exit.ico'), "Закрыть", self)
        openAction.setToolTip('Открыть рабочую область')
        saveActionAs.setToolTip('Сохранить рабочую область')
        saveActionAs.setToolTip('Сохранить рабочую область как...')
        closeAction.setToolTip('Закрыть рабочую область')
        openAction.setStatusTip('Открыть рабочую область')
        closeAction.setStatusTip('Закрыть рабочую область')


        toolBar.addAction(openAction)
        toolBar.addAction(saveAction)
        toolBar.addAction(saveActionAs)
        toolBar.addAction(closeAction)
        self.addToolBar(toolBar)
        toolBar.show()

        closeAction.triggered.connect(self.closeMdiArea)
        openAction.triggered.connect(self.openImages)

    def _createMenuBar(self):
        openAction = QAction(QIcon(self.icoDir + '16x16\\open.ico'),'Открыть', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Открыть рабочую область')

        closeAction = QAction(QIcon(self.icoDir + '16x16\\exit.ico'), 'Закрыть', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Закрыть откртый проект')
        closeAction.triggered.connect(self.closeMdiArea)

        exitAction = QAction(QIcon(self.icoDir + '16x16\\delete.ico'), 'Выход', self)
        exitAction.setShortcut('Esc')
        exitAction.setStatusTip('Выйти из программы')
        exitAction.triggered.connect(self.close)

        aboutAction = QAction(text='О программе', parent=self)
        aboutAction.setStatusTip('Информация о текущей версии программы')

        helpAction = QAction(text='Помощь', parent=self)
        helpAction.setStatusTip('Помощь по программе')

        cascadeAction = QAction(text='Каскадный', parent=self)
        tileAction = QAction(text='Мозаичный', parent=self)
        viewImage = QAction(text='Подробно', parent=self)

        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('Файл')
        viewMenu = menuBar.addMenu('Вид')
        helpMenu = menuBar.addMenu('Справка')

        fileMenu.addAction(openAction)
        fileMenu.addAction(closeAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        viewMenu.addAction(cascadeAction)
        viewMenu.addAction(tileAction)
        viewMenu.addAction(viewImage)

        helpMenu.addAction(aboutAction)
        helpMenu.addAction(helpAction)

        openAction.triggered.connect(self.openImages)
        cascadeAction.triggered.connect(self.cascadeView)
        tileAction.triggered.connect(self.tileView)
        viewImage.triggered.connect(self.openViewImage)

    def saveWorkArea(self):
        QFileDialog.getSaveFileName(self)

    def openImages(self):
        fileName = QFileDialog.getOpenFileName(self, 'Открыть область', CUREENT_DIR, 'CSV (*.csv)')
        self.centralArea = QMdiArea()
        self.setCentralWidget(self.centralArea)
        self.ivImage = {}
        csvr = csvReading(fileName[0])
        for i in csvr.fileList:
            sub = QMdiSubWindow()
            img = QLabel()
            pixmapImage = QPixmap(CUREENT_DIR + '\\images\\infra\\' + i[0])
            self.ivImage[i[0]] = (infraImage(CUREENT_DIR + '\\images\\infra\\' + i[0], i[1], i[2]),
                                       visibleImage(CUREENT_DIR + '\\images\\visible\\' + i[0]))
            img.setPixmap(pixmapImage)
            sub.setFixedHeight(240)
            sub.setFixedWidth(320)
            sub.setWidget(img)
            sub.setWindowTitle(i[0])
            self.centralArea.addSubWindow(sub)
            sub.show()

    def cascadeView(self):
        self.centralArea.cascadeSubWindows()

    def tileView(self):
        self.centralArea.tileSubWindows()

    def openViewImage(self):
        subWindow = self.centralArea.activeSubWindow()
        title = subWindow.windowTitle()
        self.aboutImage = centralWidget(self.ivImage, title)
        self.aboutImage.setMinimumHeight(600)
        self.aboutImage.setMinimumWidth(800)
        self.aboutImage.show()

    def closeMdiArea(self):
        self.centralArea.close()
