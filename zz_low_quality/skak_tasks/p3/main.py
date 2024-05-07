from PIL import Image
import numpy as np

import sys
from PySide6.QtGui import QPixmap, QAction, QColor, QPainter, QTransform
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QStackedLayout,QLineEdit, QGridLayout, QLabel,QTableWidget, QTableWidgetItem, QFileDialog,QTableView
from PySide6.QtCore import Qt,QAbstractTableModel



class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]
            if isinstance(value, float):
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
        
        self.menu = self.menuBar()
        self.viewMenu = self.menu.addMenu("Меню")
        
        self.switchAction1 = QAction("Ввод кратинки", self)
        self.switchAction1.triggered.connect(self.switch_layout_input)
        self.viewMenu.addAction(self.switchAction1)
        
        self.switchAction2 = QAction("Обучающая матрица", self)
        self.switchAction2.triggered.connect(self.switch_layout_table)
        self.viewMenu.addAction(self.switchAction2)

        self.switchAction3 = QAction("Бинарная матрица", self)
        self.switchAction3.triggered.connect(self.switch_layout_table2)
        self.viewMenu.addAction(self.switchAction3)

        self.switchAction4 = QAction("Картинка по бинарной матрице", self)
        self.switchAction4.triggered.connect(self.switch_layout_pic2)
        self.viewMenu.addAction(self.switchAction4)
        
#-----------------------------------------------------------
        self.layout_input = QGridLayout()

        self.picture_out1 = QLabel()
        self.picture_out1.setScaledContents(True);
        self.picture_out1.setMinimumSize(600, 600)
        self.layout_input.addWidget( self.picture_out1)

        self.button = QPushButton("Загрузить картинку")
        self.button.clicked.connect(self.f1)
        self.layout_input.addWidget(self.button)
        
        self.widget_input = QWidget()
        self.widget_input.setLayout(self.layout_input)
        self.layout_stack.addWidget(self.widget_input)

#-----------------------------------------------------------
        self.layout_table = QGridLayout()


        self.widget_table = QWidget()
        self.widget_table.setLayout(self.layout_table)
        self.layout_stack.addWidget(self.widget_table)
#-----------------------------------------------------------
        self.layout_table2 = QGridLayout()

        self.widget_table2 = QWidget()
        self.widget_table2.setLayout(self.layout_table2)
        self.layout_stack.addWidget(self.widget_table2)
#-----------------------------------------------------------
        self.layout_pic2 = QGridLayout()
        
        self.picture_out2 = QLabel()
        self.picture_out2.setScaledContents(True);
        self.picture_out2.setMinimumSize(600, 600)
        self.layout_pic2.addWidget( self.picture_out2)

        self.widget_pic2 = QWidget()
        self.widget_pic2.setLayout(self.layout_pic2)
        self.layout_stack.addWidget(self.widget_pic2)
#-----------------------------------------------------------

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout_stack)
        self.setCentralWidget(self.central_widget)
        

    def switch_layout_input(self):
        self.layout_stack.setCurrentIndex(0)

    def switch_layout_table(self):
        self.layout_stack.setCurrentIndex(1)
        
    def switch_layout_table2(self):
        self.layout_stack.setCurrentIndex(2)

    def switch_layout_pic2(self):
        self.layout_stack.setCurrentIndex(3)
                
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
        
        self.picture_out1.setPixmap(pixmap)

        self.table = QTableView()
        self.model = TableModel(matrix_str)
        self.table.setModel(self.model)
        self.layout_table.addWidget( self.table)
        
        delta = 50
        matrix2 = matrix1
        for i,e in enumerate(matrix1):
            print(e)
            avrg = np.mean(e)
            avrg1= avrg - delta
            print(avrg, avrg1)
            for ii,ee in enumerate(e):
                if ee <= avrg and ee >= avrg1:
                    matrix2[i][ii] = 1
                else:
                    matrix2[i][ii] = 0
        print(matrix2)
        
        delta2 = 0.5
        EV = []
        for i,e in enumerate(matrix2):
            tempcount = 0
            for ii,ee in enumerate(e):
                if ee == 1:
                    tempcount+=1
            if tempcount>=len(matrix2[0])/2:
                EV.append( 1 )
            else:
                EV.append( 0 )
        print(f"EV = {EV}")
                    
        
        
        self.table2 = QTableView()
        self.model2 = TableModel(matrix2)
        self.table2.setModel(self.model2)
        self.layout_table2.addWidget( self.table2)

        width = len(matrix2[0])
        height = len(matrix2)
        pixmap2 = QPixmap(width, height)
        painter = QPainter(pixmap2)
        
        for i in range(height):
            for j in range(width):
                color2 = QColor(0,0,0)
                if  matrix2[i][j] == 0:
                    color2 = QColor(255, 255, 255)
                
                #value = matrix2[i][j]
                painter.setPen(color2)
                painter.setBrush(Qt.white)
                painter.drawRect(j, i, 1, 1)

        painter.end()
        pixmap2.save("output.png")
        self.picture_out2.setPixmap(pixmap2)
        


app = QApplication(sys.argv)
window = MainWindow()
window.setMinimumSize(700, 700)
window.show()
sys.exit(app.exec())


