from PIL import Image
import numpy as np

import sys
from PySide6.QtWidgets import QApplication, QLabel, QFileDialog, QMainWindow,QGridLayout,QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QScrollArea,QApplication,QVBoxLayout, QGroupBox, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedLayout,QLineEdit, QGridLayout, QLabel,QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

#

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.layout_input = QGridLayout()
        self.label = QLabel()
        self.label.setText("--")
        #self.label.setWordWrap(True)
        self.label.setMinimumSize(1000, 700)
        
        self.button = QPushButton("Загрузить картинку")
        self.button.clicked.connect(self.f1)
        self.layout_input.addWidget(self.button)
        
        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setWidget(self.label)
        self.layout_input.addWidget(scroll_area)

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

        print(matrix1)

        self.label.setWordWrap(True)
        self.label.setText( str( np.asarray(matrix1) ) )


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


