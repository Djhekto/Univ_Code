from PIL import Image
import numpy as np

import sys
from PySide6.QtGui import QPixmap, QAction, QColor
from PySide6.QtWidgets import QStackedLayout, QScrollArea,QApplication,QVBoxLayout, QGroupBox, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedLayout,QLineEdit, QGridLayout, QLabel,QTableWidget, QTableWidgetItem,QApplication, QLabel, QFileDialog, QMainWindow,QGridLayout,QPushButton,QTableView
from PySide6.QtCore import Qt,QAbstractTableModel



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
        self.setWindowTitle("p1")
        self.layout_stack = QStackedLayout()
#------------------------------------------------------

        self.layout_input = QGridLayout()

        self.button = QPushButton("Загрузить картинку")
        self.button.clicked.connect(self.f1)
        self.layout_input.addWidget(self.button)

        
        self.menu = self.menuBar()
        self.viewMenu = self.menu.addMenu("Меню")
        
        self.switchAction1 = QAction("Ввод кратинки", self)
        self.switchAction1.triggered.connect(self.switch_layout_input)
        self.viewMenu.addAction(self.switchAction1)
        
        self.switchAction2 = QAction("таблица", self)
        self.switchAction2.triggered.connect(self.switch_layout_table)
        self.viewMenu.addAction(self.switchAction2)

        self.widget_input = QWidget()
        self.widget_input.setLayout(self.layout_input)
        self.layout_stack.addWidget(self.widget_input)
#-----------------------------------------------------------

        self.layout_table = QGridLayout()


        self.widget_table = QWidget()
        self.widget_table.setLayout(self.layout_table)
        self.layout_stack.addWidget(self.widget_table)
#-----------------------------------------------------------
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout_stack)
        self.setCentralWidget(self.central_widget)
        

    def switch_layout_input(self):
        self.layout_stack.setCurrentIndex(0)

    def switch_layout_table(self):
        self.layout_stack.setCurrentIndex(1)
        
    def f1(self, checked):
        
        file_path, _ = QFileDialog.getOpenFileName(filter="Images (*.png *.xpm *.jpg)")

        image_1 = Image.open(file_path)
        pixmap = QPixmap(file_path)
        
        image_1 = image_1.convert("L")
        array1 = np.array(image_1)
        matrix1 = array1
        np.set_printoptions(threshold=np.inf)

        matrix1 = np.asarray(matrix1)

        print(matrix1)
        
        matrix_str = np.array(matrix1)
        
        self.picture_out1 = QLabel()
        self.picture_out1.setScaledContents(True);
        self.picture_out1.setMinimumSize(600, 600)

        self.picture_out1.setPixmap(pixmap)
        self.layout_input.addWidget( self.picture_out1)

        self.table = QTableView()
        self.model = TableModel(matrix_str)
        self.table.setModel(self.model)
        self.layout_input.addWidget( self.table)
        self.layout_table.addWidget( self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.setMinimumSize(700, 700)
window.show()
sys.exit(app.exec())


