from PIL import Image
import numpy as np

import sys
from PySide6.QtWidgets import QApplication, QLabel, QFileDialog, QMainWindow,QGridLayout,QPushButton,QTableView
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QScrollArea,QApplication,QVBoxLayout, QGroupBox, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedLayout,QLineEdit, QGridLayout, QLabel,QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt,QAbstractTableModel

#
class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]
            if isinstance(value, float):
                # Render float to 2 dp
                return "%.6f" % value
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.layout_input = QGridLayout()

        self.button = QPushButton("Загрузить картинку")
        self.button.clicked.connect(self.f1)
        self.layout_input.addWidget(self.button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout_input)
        self.setCentralWidget(self.central_widget)

    def f1(self, checked):
        
        file_path, pic = QFileDialog.getOpenFileName(filter="Images (*.png *.xpm *.jpg)")
        pixmap = QPixmap(pic)

        image_1 = Image.open(file_path)
        image_1 = image_1.convert("L")
        array1 = np.array(image_1)
        matrix1 = array1 / 255.0
        np.set_printoptions(threshold=np.inf)

        matrix1 = np.asarray(matrix1)

        print(matrix1)
        
        matrix_str = np.array(matrix1)
        
        self.table = QTableView()
        self.model = TableModel(matrix_str)
        self.table.setModel(self.model)
        self.layout_input.addWidget( self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())



##
image_2 = Image.open("2.png")
image_2 = image_2.convert("L")
array2 = np.array(image_2)
matrix2 = array2 / 255.0
print(matrix2)


