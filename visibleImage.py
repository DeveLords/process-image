# Наследуемый класс для видимого изображения
# от базового класса image

from image import image
import numpy

class visibleImage(image):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
