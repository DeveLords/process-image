from PySide6.QtWidgets import (QWidget,
                               QLabel,
                               QHBoxLayout,
                               QVBoxLayout,
                               QPushButton,
                               QGroupBox,
                               QSizePolicy,
                               QRadioButton,
                               QCheckBox,
                               QDoubleSpinBox)
from PySide6 import QtWidgets, QtCore

from processImageModel import processImageModel

class centralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._createСentralWidget()

    def _createСentralWidget(self):
        
        self.processImageModel = processImageModel()
        # Левая секция окна
        self.imageView = QLabel()
        self.tableInfAboutImage = QtWidgets.QTableView()
        self.tableInfAboutImage.setModel(self.processImageModel)
    
        self.imageView.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.tableInfAboutImage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Правая секция окна
        self.displayGroupBox = QGroupBox('Отображение', self)
        self.rangeGroupBox = QGroupBox('Диапазоны', self)
        self.dotGroupBox = QGroupBox('Точки', self)
        self.areaGroupBox = QGroupBox('Области', self)

        # Макеты групбоксов
        diplayGroupBoxLayout = QVBoxLayout()
        rangeGroupBoxVLayout_1 = QVBoxLayout()
        rangeGroupBoxVLayout_2 = QVBoxLayout()
        rangeGroupBoxHLayout = QHBoxLayout()
        dotGroupBoxLayout = QVBoxLayout()
        areaGroupBoxLayout = QVBoxLayout()

        # displayGroupBox Груп бок отображений
        self.infraredDisplaying = QRadioButton('Инфракрасное', self.displayGroupBox)
        self.infraredDisplaying.setCheckable(True)
        self.infraredDisplaying.setChecked(True)
        self.infraredDisplaying.setStatusTip('Режим отображения: инфракрасное изображение')
        
        self.visibleDisplaying = QRadioButton('Видимое', self.displayGroupBox)
        self.visibleDisplaying.setCheckable(True)
        self.visibleDisplaying.setStatusTip('Режим отображения: изображение в видимом диапазоне')
        
        self.infraredDisplaying.clicked.connect(self.turnDisplay)
        self.visibleDisplaying.clicked.connect(self.turnDisplay)

        # rangeGroupBox
        self.minRangeLabel = QLabel('Минимум', self)
        self.maxRangeLabel = QLabel('Максимум', self)
        self.rangeMin = QDoubleSpinBox(self)
        self.rangeMax = QDoubleSpinBox(self)
        
        self.applyButton = QPushButton('Принять',self)
        self.resetButton = QPushButton('Сбросить',self)
        self.applyButton.setStatusTip('Применить новый диапазон отображаемых температур')
        self.resetButton.setStatusTip('Сбросить диапазон отображаемых температур')
        
        self.applyButton.pressed.connect(self.changeRangeTemp)
        self.resetButton.pressed.connect(self.resetRangeTemp)
        # dotGroupBox
        self.hotDot = QRadioButton('Горячая', self)
        self.coldDot = QRadioButton('Холодная', self)
        self.avgDot = QRadioButton('Средняя', self)
        
        self.hotDot.setCheckable(True)
        self.coldDot.setCheckable(True)
        self.avgDot.setCheckable(True)
        
        self.hotDot.clicked.connect(self.dotTypeDisplay)
        self.coldDot.clicked.connect(self.dotTypeDisplay)
        self.avgDot.clicked.connect(self.dotTypeDisplay)
        

        #areaGroupBox
        self.originalArea = QRadioButton('Оригинал', self)
        self.coldArea = QRadioButton('Холодные', self)
        self.hotArea = QRadioButton('Горячие', self)
        self.avgArea = QRadioButton('Средних', self)
        
        self.originalArea.setStatusTip('Показать изначальное изображение')
        self.coldArea.setStatusTip('Показать холодные области')
        self.hotArea.setStatusTip('Показать горячие области')
        self.avgArea.setStatusTip('Пока области средних температур')
        
        
        self.originalArea.clicked.connect(self.infraTypeDisplay)
        self.coldArea.clicked.connect(self.infraTypeDisplay)
        self.hotArea.clicked.connect(self.infraTypeDisplay)
        self.avgArea.clicked.connect(self.infraTypeDisplay)

        self.originalArea.setCheckable(True)
        self.originalArea.setChecked(True)
        self.coldArea.setCheckable(True)
        self.hotArea.setCheckable(True)
        self.avgArea.setCheckable(True)


        #Добавлене виджетов
        diplayGroupBoxLayout.addWidget(self.infraredDisplaying)
        diplayGroupBoxLayout.addWidget(self.visibleDisplaying)

        rangeGroupBoxVLayout_1.addWidget(self.minRangeLabel)
        rangeGroupBoxVLayout_1.addWidget(self.rangeMin)
        rangeGroupBoxVLayout_1.addWidget(self.applyButton)

        rangeGroupBoxVLayout_2.addWidget(self.maxRangeLabel)
        rangeGroupBoxVLayout_2.addWidget(self.rangeMax)
        rangeGroupBoxVLayout_2.addWidget(self.resetButton)

        dotGroupBoxLayout.addWidget(self.hotDot)
        dotGroupBoxLayout.addWidget(self.coldDot)
        dotGroupBoxLayout.addWidget(self.avgDot)

        areaGroupBoxLayout.addWidget(self.originalArea)
        areaGroupBoxLayout.addWidget(self.hotArea)
        areaGroupBoxLayout.addWidget(self.coldArea)
        areaGroupBoxLayout.addWidget(self.avgArea)

        rangeGroupBoxHLayout.addLayout(rangeGroupBoxVLayout_1)
        rangeGroupBoxHLayout.addLayout(rangeGroupBoxVLayout_2)

        # Применение макета
        self.displayGroupBox.setLayout(diplayGroupBoxLayout)
        self.rangeGroupBox.setLayout(rangeGroupBoxHLayout)
        self.dotGroupBox.setLayout(dotGroupBoxLayout)
        self.areaGroupBox.setLayout(areaGroupBoxLayout)

        # Главный макет
        mainHLayout = QHBoxLayout()
        mainLeftVLayout = QVBoxLayout()
        mainLeftBHLayout = QHBoxLayout()
        mainRightVLayout = QVBoxLayout()

        # Настройка левой секции
        # mainLeftBHLayout.addWidget(self.previousButton)
        # mainLeftBHLayout.addWidget(self.nextButton)
        mainLeftVLayout.addWidget(self.imageView)
        mainLeftVLayout.addWidget(self.tableInfAboutImage)
        mainLeftVLayout.addLayout(mainLeftBHLayout)

        # Настройка правой секции
        mainRightVLayout.addWidget(self.displayGroupBox)
        mainRightVLayout.addWidget(self.rangeGroupBox)
        mainRightVLayout.addWidget(self.dotGroupBox)
        mainRightVLayout.addWidget(self.areaGroupBox)

        mainHLayout.addLayout(mainLeftVLayout)
        mainHLayout.addLayout(mainRightVLayout)

        self.setLayout(mainHLayout)

    def turnDisplay(self):
        print(self.infraredDisplaying.isChecked())
        image = self.processImageModel.showSelectedImage(self.currentIndex, self.infraredDisplaying.isChecked())
        
        self.imageView.setPixmap(image)
        self.processImageModel.layoutChanged.emit()
        self.rangeMin.setValue(self.processImageModel.imageInf[0][1])
        self.rangeMax.setValue(self.processImageModel.imageInf[0][2])
        
    def changeRangeTemp(self):
        tempMin = self.rangeMin.value()
        tempMax = self.rangeMax.value()
        image = self.processImageModel.ProcessImage(self.currentIndex, 5, tempMin, tempMax)
        self.imageView.setPixmap(image)
        self.rangeMin.setMaximum(self.rangeMax.value())
        self.rangeMax.setMaximum(self.rangeMax.value() + 200)
    
    def resetRangeTemp(self):
        image = self.processImageModel.showSelectedImage(self.currentIndex, self.infraredDisplaying.isChecked())
        self.imageView.setPixmap(image)
        self.rangeMin.setValue(self.processImageModel.imageInf[0][1])
        self.rangeMax.setValue(self.processImageModel.imageInf[0][2])
        self.rangeMin.setMaximum(self.rangeMax.value())
        self.rangeMax.setMaximum(self.rangeMax.value() + 200)
    
    def infraTypeDisplay(self):
        if self.originalArea.isChecked() is True:
            typeDisplay = 1
        if self.hotArea.isChecked() is True:
            typeDisplay = 2
        if self.coldArea.isChecked() is True:
            typeDisplay = 3
        if self.avgArea.isChecked() is True:
            typeDisplay = 4      
        image = self.processImageModel.ProcessImage(self.currentIndex, typeDisplay)
        self.imageView.setPixmap(image)
    
    def dotTypeDisplay(self):
        if self.hotDot.isChecked() is True:
            typeDisplay = 6
        if self.coldDot.isChecked() is True:
            typeDisplay = 7
        if self.avgDot.isChecked() is True:
            typeDisplay = 8
        image = self.processImageModel.ProcessImage(self.currentIndex, typeDisplay)
        self.imageView.setPixmap(image)
        
    
    def setImageContainerModel(self, imageContainer):
        self.processImageModel.setImageContainer(imageContainer)
        
    def showSelectedImage(self, index):
        self.currentIndex = index
        image = self.processImageModel.showSelectedImage(self.currentIndex, self.infraredDisplaying.isChecked())
        self.imageView.setPixmap(image)
        self.processImageModel.layoutChanged.emit()
        self.rangeMin.setValue(self.processImageModel.imageInf[0][1])
        self.rangeMax.setValue(self.processImageModel.imageInf[0][2])
        self.rangeMin.setMaximum(self.rangeMax.value())
        self.rangeMin.setMaximum(self.processImageModel.imageInf[0][1] + 200)
        
    def clearArea(self):
        self.imageView.clear()
        self.rangeMin.clear()
        self.rangeMax.clear()
        self.processImageModel.clearData()
        self.processImageModel.layoutChanged.emit()
