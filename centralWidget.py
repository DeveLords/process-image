from PySide6.QtWidgets import (QWidget,
                               QLabel,
                               QHBoxLayout,
                               QVBoxLayout,
                               QTableWidget,
                               QPushButton,
                               QGroupBox,
                               QSizePolicy,
                               QRadioButton,
                               QCheckBox,
                               QDoubleSpinBox,
                               QTableWidgetItem)
from PySide6.QtCore import Qt

class centralWidget(QWidget):
    def __init__(self, ivImage : dict, fileName : str):
        super().__init__()
        self.ivImage = ivImage
        self.fileName = fileName
        self.listKeys = list(self.ivImage)
        self.ind = self.listKeys.index(self.fileName)
        self.setWindowTitle('Подробно')
        self._createСentralWidget()

    def _createСentralWidget(self):
        # Левая секция окна
        self.imageView = QLabel()
        self.tableInfAboutImage = QTableWidget(self)
        image = self.ivImage[self.fileName][0].convertCV2toQt()
        self.imageView.setPixmap(image)
        self.imageView.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableInfAboutImage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.tableInfAboutImage.setColumnCount(3)
        self.tableInfAboutImage.setRowCount(2)
        self.tableInfAboutImage.setItem(0, 0, QTableWidgetItem('Имя файла'))
        self.tableInfAboutImage.setItem(0, 1, QTableWidgetItem('Минимум'))
        self.tableInfAboutImage.setItem(0, 2, QTableWidgetItem('Максимум'))
        self.fillTable()

        self.previousButton = QPushButton(text='<-- Предудующее', parent=self)
        self.nextButton = QPushButton(text='Следующее -->', parent=self)
        self.previousButton.clicked.connect(self.clikedPreviousBtn)
        self.nextButton.clicked.connect(self.clikedNextBtn)

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
        self.visibleDisplaying = QRadioButton('Видимое', self.displayGroupBox)
        self.visibleDisplaying.setCheckable(True)
        self.infraredDisplaying.clicked.connect(self.turnVisInfra)
        self.visibleDisplaying.clicked.connect(self.turnInfraVis)

        # rangeGroupBox
        self.minRangeLabel = QLabel('Минимум', self)
        self.maxRangeLabel = QLabel('Максимум', self)
        self.rangeMin = QDoubleSpinBox(self)
        self.rangeMin.setValue(self.ivImage[self.fileName][0].getTempMin())
        self.rangeMax = QDoubleSpinBox(self)
        self.rangeMax.setValue(self.ivImage[self.fileName][0].getTempMax())
        self.applyButton = QPushButton('Принять',self)
        self.resetButton = QPushButton('Сбросить',self)

        # dotGroupBox
        self.hotDot = QCheckBox('Горячая', self)
        self.coldDot = QCheckBox('Холодная', self)
        self.avgDot = QCheckBox('Средняя', self)

        #areaGroupBox
        self.originalArea = QRadioButton('Оригинал', self)
        self.coldArea = QRadioButton('Холодные', self)
        self.hotArea = QRadioButton('Горячие', self)
        self.avgArea = QRadioButton('Средних', self)

        self.originalArea.setCheckable(True)
        self.originalArea.setChecked(True)


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
        mainLeftBHLayout.addWidget(self.previousButton)
        mainLeftBHLayout.addWidget(self.nextButton)
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

    def turnInfraVis(self):
        image = self.ivImage[self.fileName][1].convertCV2toQt()
        self.imageView.setPixmap(image)
        self.rangeGroupBox.setEnabled(False)
        self.dotGroupBox.setEnabled(False)
        self.areaGroupBox.setEnabled(False)

    def turnVisInfra(self):
        image = self.ivImage[self.fileName][0].convertCV2toQt()
        self.imageView.setPixmap(image)
        self.rangeGroupBox.setEnabled(True)
        self.dotGroupBox.setEnabled(True)
        self.areaGroupBox.setEnabled(True)

    def setNewPixmap(self):
        if self.infraredDisplaying.isChecked() is True:
            image = self.ivImage[self.fileName][0].convertCV2toQt()
            self.imageView.setPixmap(image)
            self.imageView.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.rangeMin.setValue(self.ivImage[self.fileName][0].getTempMin())
            self.rangeMax.setValue(self.ivImage[self.fileName][0].getTempMax())
        else:
            image = self.ivImage[self.fileName][1].convertCV2toQt()
            self.imageView.setPixmap(image)
            self.imageView.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.rangeMin.setValue(self.ivImage[self.fileName][0].getTempMin())
            self.rangeMax.setValue(self.ivImage[self.fileName][0].getTempMax())

    def clikedPreviousBtn(self):
        self.ind -= 1
        if self.ind >= 0:
            self.fileName = self.listKeys[self.ind]
            self.setNewPixmap()
            self.fillTable()
        else:
            self.ind = (len(self.listKeys) - 1)
            self.fileName = self.listKeys[self.ind]
            self.setNewPixmap()
            self.fillTable()

    def clikedNextBtn(self):
        self.ind += 1
        if self.ind != len(self.listKeys):
            self.fileName = self.listKeys[self.ind]
            self.setNewPixmap()
            self.fillTable()
        else:
            self.ind = 0
            self.fileName = self.listKeys[self.ind]
            self.setNewPixmap()
            self.fillTable()

    def fillTable(self):
        self.tableInfAboutImage.setItem(1, 0, QTableWidgetItem(self.fileName))
        self.tableInfAboutImage.setItem(1, 1, QTableWidgetItem(str(self.ivImage[self.fileName][0].getTempMin())))
        self.tableInfAboutImage.setItem(1, 2, QTableWidgetItem(str(self.ivImage[self.fileName][0].getTempMax())))
