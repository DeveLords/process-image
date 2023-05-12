import csv

class csvReading:
    def __init__(self, fileNameCSV) -> None:
        self.fileList = list()
        with open(fileNameCSV, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=';')
            next(file_reader)
            for raw in file_reader:
                fileName = raw[0][-12:].replace('IS2', 'bmp')
                coldPoint = float(raw[4].replace(',', '.'))
                hotpoint = float(raw[5].replace(',', '.'))
                self.fileList.append((fileName, coldPoint, hotpoint))
