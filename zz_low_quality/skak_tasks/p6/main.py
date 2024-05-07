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
    counter_for_button_press = 0

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
        
        self.switchAction2 = QAction("Обучающая матрица 1", self)
        self.switchAction2.triggered.connect(self.switch_layout_table1)
        self.viewMenu.addAction(self.switchAction2)

        self.switchAction3 = QAction("Бинарная матрица 1", self)
        self.switchAction3.triggered.connect(self.switch_layout_table1new)
        self.viewMenu.addAction(self.switchAction3)

        self.switchAction4 = QAction("Картинка по бинарной матрице", self)
        self.switchAction4.triggered.connect(self.switch_layout_pic1new)
        self.viewMenu.addAction(self.switchAction4)
        
        self.switchAction5 = QAction("SK, SKPARA", self)
        self.switchAction5.triggered.connect(self.skparadisplay)
        self.viewMenu.addAction(self.switchAction5)
        
#-----------------------------------------------------------
        self.layout_input = QGridLayout()

        self.picture_out1 = QLabel()
        #self.picture_out1.setScaledContents(True);
        self.picture_out1.setMinimumSize(114, 114)
        self.layout_input.addWidget( self.picture_out1, 0 ,1)
        
        self.picture_out2 = QLabel()
        #self.picture_out2.setScaledContents(True);
        self.picture_out2.setMinimumSize(114, 114)
        self.layout_input.addWidget( self.picture_out2, 0, 2)

        self.picture_out3 = QLabel()
        #self.picture_out3.setScaledContents(True);
        self.picture_out3.setMinimumSize(114, 114)
        self.layout_input.addWidget( self.picture_out3, 0, 3)

        self.picture_out1c = QLabel()
        #self.picture_out1c.setScaledContents(True);
        self.picture_out1c.setMinimumSize(114, 114)
        self.layout_input.addWidget( self.picture_out1c, 1 ,0)
        
        self.picture_out2c = QLabel()
        #self.picture_out2c.setScaledContents(True);
        self.picture_out2c.setMinimumSize(114, 114)
        self.layout_input.addWidget( self.picture_out2c, 2, 0)

        self.picture_out3c = QLabel()
        #self.picture_out3c.setScaledContents(True);
        self.picture_out3c.setMinimumSize(114, 114)
        self.layout_input.addWidget( self.picture_out3c, 3, 0)
        
        self.r12 = QLabel()
        self.layout_input.addWidget( self.r12, 1, 2)
        self.r13 = QLabel()
        self.layout_input.addWidget( self.r13, 1, 3)
        self.r21 = QLabel()
        self.layout_input.addWidget( self.r21, 2, 1)
        self.r23 = QLabel()
        self.layout_input.addWidget( self.r23, 2, 3)
        self.r31 = QLabel()
        self.layout_input.addWidget( self.r31, 3, 1)
        self.r32 = QLabel()
        self.layout_input.addWidget( self.r32, 3, 2)


        self.button = QPushButton("Загрузить картинку")
        self.button.setMaximumSize(114, 114)
        #self.button.resize(114, 100)
        self.button.clicked.connect(self.switch_functions)
        self.layout_input.addWidget(self.button, 0 ,0)
        
        self.button2 = QPushButton("Посчитать кодовые расстояния")
        self.button2.clicked.connect(self.pkrf1)
        self.layout_input.addWidget(self.button2, 4 ,0)
        
        self.widget_input = QWidget()
        self.widget_input.setLayout(self.layout_input)
        self.layout_stack.addWidget(self.widget_input)

#-----------------------------------------------------------
        self.layout_table1 = QGridLayout()

        self.widget_table1 = QWidget()
        self.widget_table1.setLayout(self.layout_table1)
        self.layout_stack.addWidget(self.widget_table1)
#-----------------------------------------------------------
        self.layout_table1new = QGridLayout()

        self.widget_table1new = QWidget()
        self.widget_table1new.setLayout(self.layout_table1new)
        self.layout_stack.addWidget(self.widget_table1new)
#-----------------------------------------------------------
        self.layout_pic1new = QGridLayout()
        
        self.picture_out1new = QLabel()
        self.picture_out1new.setScaledContents(True);
        self.picture_out1new.setMinimumSize(600, 600)
        self.layout_pic1new.addWidget( self.picture_out1new)

        self.widget_pic1new = QWidget()
        self.widget_pic1new.setLayout(self.layout_pic1new)
        self.layout_stack.addWidget(self.widget_pic1new)
#-----------------------------------------------------------
        self.layout_skres = QGridLayout()
        
        self.sktextout = QLabel()
        self.sktextout.setScaledContents(True);
        self.sktextout.setMaximumSize(600, 600)
        self.layout_skres.addWidget( self.sktextout )

        self.widget_skres = QWidget()
        self.widget_skres.setLayout(self.layout_skres)
        self.layout_stack.addWidget(self.widget_skres)

#----------------------------------------------------------
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout_stack)
        self.setCentralWidget(self.central_widget)
        

    def switch_layout_input(self):
        self.layout_stack.setCurrentIndex(0)

    def switch_layout_table1(self):
        self.layout_stack.setCurrentIndex(1)
        
    def switch_layout_table1new(self):
        self.layout_stack.setCurrentIndex(2)

    def switch_layout_pic1new(self):
        self.layout_stack.setCurrentIndex(3)
    
    def skparadisplay(self):
        self.layout_stack.setCurrentIndex(4)

    
    def switch_functions(self):
        np.set_printoptions(threshold=np.inf)

        image_1 = Image.open("1k.png")
        image_1 = image_1.convert("L")
        matrix1 = np.asarray(np.array(image_1))
        image_2 = Image.open("2k.png")
        image_2 = image_2.convert("L")
        matrix2 = np.asarray(np.array(image_2))
        image_3 = Image.open("4k.png")
        image_3 = image_3.convert("L")
        matrix3 = np.asarray(np.array(image_3))
        #delta = 40
        bestkfe = -1

        for delta in range(30,71,10):
            weshouldbreakthings = False
            weshouldconsiderbreaking = False
            for ro_1 in range(40,61,10):
                nro_1 = ro_1/100
                if weshouldbreakthings:
                    break
                for ro_2 in range(40,61,10):
                    nro_2 = ro_2/100
                    if weshouldbreakthings:
                        break
                    for ro_3 in range(40,61,10):
                        if weshouldbreakthings:
                            break
                        nro_3 = ro_3/100
                                        
                        self.matrixbin1 = matrix1
                        for i,e in enumerate(matrix1):
                            #print(e)
                            avrg = np.mean(e)
                            avrg1= avrg - delta
                            #print(avrg, avrg1)
                            for ii,ee in enumerate(e):
                                if ee <= avrg and ee >= avrg1:
                                    self.matrixbin1[i][ii] = 1
                                else:
                                    self.matrixbin1[i][ii] = 0
                                    
                        self.EV1 = []
                        for i,e in enumerate(self.matrixbin1):
                            tempcount = 0
                            for ii,ee in enumerate(e):
                                if ee == 1:
                                    tempcount+=1
                            if tempcount>= (len(self.matrixbin1[0])*nro_1):
                                self.EV1.append( 1 )
                            else:
                                self.EV1.append( 0 )

                        self.matrixbin2 = matrix2
                        for i,e in enumerate(matrix2):
                            avrg = np.mean(e)
                            avrg1= avrg - delta
                            for ii,ee in enumerate(e):
                                if ee <= avrg and ee >= avrg1:
                                    self.matrixbin2[i][ii] = 1
                                else:
                                    self.matrixbin2[i][ii] = 0

                        self.EV2 = []
                        for i,e in enumerate(self.matrixbin2):
                            tempcount = 0
                            for ii,ee in enumerate(e):
                                if ee == 1:
                                    tempcount+=1
                            if tempcount>= (len(self.matrixbin2[0])*nro_2):
                                self.EV2.append( 1 )
                            else:
                                self.EV2.append( 0 )

                        self.matrixbin3 = matrix3
                        for i,e in enumerate(matrix3):
                            avrg = np.mean(e)
                            avrg1= avrg - delta
                            for ii,ee in enumerate(e):
                                if ee <= avrg and ee >= avrg1:
                                    self.matrixbin3[i][ii] = 1
                                else:
                                    self.matrixbin3[i][ii] = 0

                        self.EV3 = []
                        for i,e in enumerate(self.matrixbin3):
                            tempcount = 0
                            for ii,ee in enumerate(e):
                                if ee == 1:
                                    tempcount+=1
                            if tempcount>= (len(self.matrixbin3[0])*nro_3):
                                self.EV3.append( 1 )
                            else:
                                self.EV3.append( 0 )

                        #print(f"EV1 = {self.EV1}")                
                        #print(f"EV2 = {self.EV2}")                
                        #print(f"EV3 = {self.EV3}") 
                        
                        if self.EV1 == self.EV2 and  self.EV1 == self.EV3:
                            if   weshouldconsiderbreaking:
                                weshouldbreakthings = True
                                print("br")
                            #ro_1 +=10
                            weshouldconsiderbreaking = True
                            break 
                        else:
                            weshouldconsiderbreaking = False




                        self.SK1_short     = []
                        self.pkrf1_strout = ""

                        list_append_me = []        
                        for i,e in enumerate(self.EV1):
                            counter_append_me = 0
                            for ee in self.matrixbin1[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK1_short.append(list_append_me)

                        list_append_me = []        
                        for i,e in enumerate(self.EV1):
                            counter_append_me = 0
                            for ee in self.matrixbin2[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK1_short.append(list_append_me)
                        
                        list_append_me = []        
                        for i,e in enumerate(self.EV1):
                            counter_append_me = 0
                            for ee in self.matrixbin3[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK1_short.append(list_append_me)
                        
                        #print(f"Кодовое расстояние между EV1 и бинарными матрицами 1,2,3 соответственно: \n{self.SK1_short[0]}\n{self.SK1_short[1]}\n{self.SK1_short[2]}")        
                        #self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV1 и бинарными матрицами 1,2,3 соответственно: \n{self.SK1_short[0]}\n{self.SK1_short[1]}\n{self.SK1_short[2]}"+"\n"
                        
                        self.SK2_short     = []

                        list_append_me = []        
                        for i,e in enumerate(self.EV2):
                            counter_append_me = 0
                            for ee in self.matrixbin1[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK2_short.append(list_append_me)

                        list_append_me = []        
                        for i,e in enumerate(self.EV2):
                            counter_append_me = 0
                            for ee in self.matrixbin2[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK2_short.append(list_append_me)
                        
                        list_append_me = []        
                        for i,e in enumerate(self.EV2):
                            counter_append_me = 0
                            for ee in self.matrixbin3[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK2_short.append(list_append_me)
                        
                        #print(f"Кодовое расстояние между EV2 и бинарными матрицами 1,2,3 соответственно: \n{self.SK2_short[0]}\n{self.SK2_short[1]}\n{self.SK2_short[2]}")        
                        #self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV2 и бинарными матрицами 1,2,3 соответственно: \n{self.SK2_short[0]}\n{self.SK2_short[1]}\n{self.SK2_short[2]}"+"\n"
                        
                        self.SK3_short     = []

                        list_append_me = []        
                        for i,e in enumerate(self.EV3):
                            counter_append_me = 0
                            for ee in self.matrixbin1[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK3_short.append(list_append_me)

                        list_append_me = []        
                        for i,e in enumerate(self.EV3):
                            counter_append_me = 0
                            for ee in self.matrixbin2[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK3_short.append(list_append_me)
                        
                        list_append_me = []        
                        for i,e in enumerate(self.EV3):
                            counter_append_me = 0
                            for ee in self.matrixbin3[i]:
                                if e!=ee:
                                    counter_append_me += 1
                            list_append_me.append(counter_append_me)
                        self.SK3_short.append(list_append_me)
                        
                        #print(f"Кодовое расстояние между EV3 и бинарными матрицами 1,2,3 соответственно: \n{self.SK3_short[0]}\n{self.SK3_short[1]}\n{self.SK3_short[2]}")        
                        #self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV3 и бинарными матрицами 1,2,3 соответственно: \n{self.SK3_short[0]}\n{self.SK3_short[1]}\n{self.SK3_short[2]}"+"\n"

                        self.rasstoyanie12 = 0
                        for i,e in enumerate(self.SK1_short[0]):
                            if e != self.SK1_short[1][i]:
                                self.rasstoyanie12 += 1
                        #print("r12:  ",self.rasstoyanie12)
                        self.rasstoyanie13 = 0
                        for i,e in enumerate(self.SK1_short[0]):
                            if e != self.SK1_short[2][i]:
                                self.rasstoyanie13 += 1
                        #print("r13:  ",self.rasstoyanie13)

                        self.rasstoyanie21 = 0
                        for i,e in enumerate(self.SK2_short[1]):
                            if e != self.SK2_short[0][i]:
                                self.rasstoyanie21 += 1
                        #print("r21:  ",self.rasstoyanie21)
                        self.rasstoyanie23 = 0
                        for i,e in enumerate(self.SK2_short[1]):
                            if e != self.SK2_short[2][i]:
                                self.rasstoyanie23 += 1
                        #print("r23:  ",self.rasstoyanie23)

                        self.rasstoyanie31 = 0
                        for i,e in enumerate(self.SK3_short[2]):
                            if e != self.SK3_short[0][i]:
                                self.rasstoyanie31 += 1
                        #print("r31:  ",self.rasstoyanie31)
                        self.rasstoyanie32 = 0
                        for i,e in enumerate(self.SK3_short[2]):
                            if e != self.SK3_short[1][i]:
                                self.rasstoyanie32 += 1
                        #print("r32:  ",self.rasstoyanie32)
                        
                        #self.sktextout.setText(str( self.pkrf1_strout ))

                        KFE12_Shennon, KFE12_Kulbak = cnt_kfe(self.rasstoyanie12, self.SK1_short[0], self.SK1_short[1])
                        KFE13_Shennon, KFE13_Kulbak = cnt_kfe(self.rasstoyanie13, self.SK1_short[0], self.SK1_short[2])
                        bestkfe1, bestrad1 = bestkferad(KFE12_Shennon, KFE13_Shennon, min(self.rasstoyanie12, self.rasstoyanie13))

                        #print("1 KFE",bestkfe1, bestrad1,sep="\n")

                        KFE21_Shennon, KFE21_Kulbak = cnt_kfe(self.rasstoyanie21, self.SK2_short[1], self.SK2_short[0])
                        KFE23_Shennon, KFE23_Kulbak = cnt_kfe(self.rasstoyanie23, self.SK2_short[1], self.SK2_short[2])
                        bestkfe2, bestrad2 = bestkferad(KFE21_Shennon, KFE23_Shennon, min(self.rasstoyanie21, self.rasstoyanie23))
                        
                        #print("2 KFE",bestkfe2, bestrad2,sep="\n")

                        KFE31_Shennon, KFE31_Kulbak = cnt_kfe(self.rasstoyanie31, self.SK3_short[2], self.SK3_short[0])
                        KFE32_Shennon, KFE32_Kulbak = cnt_kfe(self.rasstoyanie32, self.SK3_short[2], self.SK3_short[1])
                        bestkfe3, bestrad3 = bestkferad(KFE31_Shennon, KFE32_Shennon, min(self.rasstoyanie31, self.rasstoyanie32))
                        
                        #print("3 KFE",bestkfe3, bestrad3,sep="\n")
                        
                        boolfirsteverloop = False
                        cur_kfe=bestkfe1+bestkfe2+bestkfe3
                        print(cur_kfe)

                        if (cur_kfe>bestkfe):
                            bestkfe=cur_kfe
                            sbestdelta=delta
                            sbestro1=ro_1
                            sbestro2=ro_2
                            sbestro3=ro_3
                            BESTKFE12_Shennon, BESTKFE12_Kulbak = KFE12_Shennon, KFE12_Kulbak
                            BESTKFE13_Shennon, BESTKFE13_Kulbak = KFE13_Shennon, KFE13_Kulbak
                            
                            BESTKFE21_Shennon, BESTKFE21_Kulbak = KFE21_Shennon, KFE21_Kulbak
                            BESTKFE23_Shennon, BESTKFE23_Kulbak = KFE23_Shennon, KFE23_Kulbak
                            
                            BESTKFE31_Shennon, BESTKFE31_Kulbak = KFE31_Shennon, KFE31_Kulbak
                            BESTKFE32_Shennon, BESTKFE32_Kulbak = KFE32_Shennon, KFE32_Kulbak
                            
                            self.r12.setText(str(self.rasstoyanie12))
                            self.r13.setText(str(self.rasstoyanie13))
                            self.r21.setText(str(self.rasstoyanie21))
                            self.r23.setText(str(self.rasstoyanie23))
                            self.r31.setText(str(self.rasstoyanie31))
                            self.r32.setText(str(self.rasstoyanie32))
        delta=sbestdelta
        ro1=sbestro1/100
        ro2=sbestro2/100
        ro3=sbestro3/100
        print("Конец первого этапа оптимизации")
        print(f"Лучшее значение дельта = {delta}\n")
        print(f"Лучшее значение 1 радиуса {ro1}\n")
        print(f"Лучшее значение 2 радиуса {ro2}\n")
        print(f"Лучшее значение 3 радиуса {ro3}\n")
        print(f"Лучшее значение суммы кфе Шеннона KFE {bestkfe}\n")
        print(f" оно получено из:\n BESTKFE12_Shennon = {BESTKFE12_Shennon} BESTKFE13_Shennon = {BESTKFE13_Shennon}\n")
        print(f" BESTKFE21_Shennon = {BESTKFE21_Shennon} BESTKFE23_Shennon = {BESTKFE23_Shennon}\n")
        print(f" BESTKFE31_Shennon = {BESTKFE31_Shennon} BESTKFE32_Shennon = {BESTKFE32_Shennon}\n")
        

    def pkrf1(self):
        self.SK1_short     = []
        self.pkrf1_strout = ""

        list_append_me = []        
        for i,e in enumerate(self.EV1):
            counter_append_me = 0
            for ee in self.matrixbin1[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK1_short.append(list_append_me)

        list_append_me = []        
        for i,e in enumerate(self.EV1):
            counter_append_me = 0
            for ee in self.matrixbin2[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK1_short.append(list_append_me)
        
        list_append_me = []        
        for i,e in enumerate(self.EV1):
            counter_append_me = 0
            for ee in self.matrixbin3[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK1_short.append(list_append_me)
        
        print(f"Кодовое расстояние между EV1 и бинарными матрицами 1,2,3 соответственно: \n{self.SK1_short[0]}\n{self.SK1_short[1]}\n{self.SK1_short[2]}")        
        self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV1 и бинарными матрицами 1,2,3 соответственно: \n{self.SK1_short[0]}\n{self.SK1_short[1]}\n{self.SK1_short[2]}"+"\n"
        
        self.SK2_short     = []

        list_append_me = []        
        for i,e in enumerate(self.EV2):
            counter_append_me = 0
            for ee in self.matrixbin1[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK2_short.append(list_append_me)

        list_append_me = []        
        for i,e in enumerate(self.EV2):
            counter_append_me = 0
            for ee in self.matrixbin2[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK2_short.append(list_append_me)
        
        list_append_me = []        
        for i,e in enumerate(self.EV2):
            counter_append_me = 0
            for ee in self.matrixbin3[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK2_short.append(list_append_me)
        
        print(f"Кодовое расстояние между EV2 и бинарными матрицами 1,2,3 соответственно: \n{self.SK2_short[0]}\n{self.SK2_short[1]}\n{self.SK2_short[2]}")        
        self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV2 и бинарными матрицами 1,2,3 соответственно: \n{self.SK2_short[0]}\n{self.SK2_short[1]}\n{self.SK2_short[2]}"+"\n"
        
        self.SK3_short     = []

        list_append_me = []        
        for i,e in enumerate(self.EV3):
            counter_append_me = 0
            for ee in self.matrixbin1[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK3_short.append(list_append_me)

        list_append_me = []        
        for i,e in enumerate(self.EV3):
            counter_append_me = 0
            for ee in self.matrixbin2[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK3_short.append(list_append_me)
        
        list_append_me = []        
        for i,e in enumerate(self.EV3):
            counter_append_me = 0
            for ee in self.matrixbin3[i]:
                if e!=ee:
                    counter_append_me += 1
            list_append_me.append(counter_append_me)
        self.SK3_short.append(list_append_me)
        
        print(f"Кодовое расстояние между EV3 и бинарными матрицами 1,2,3 соответственно: \n{self.SK3_short[0]}\n{self.SK3_short[1]}\n{self.SK3_short[2]}")        
        self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV3 и бинарными матрицами 1,2,3 соответственно: \n{self.SK3_short[0]}\n{self.SK3_short[1]}\n{self.SK3_short[2]}"+"\n"

        self.rasstoyanie12 = 0
        for i,e in enumerate(self.SK1_short[0]):
            if e != self.SK1_short[1][i]:
                self.rasstoyanie12 += 1
        print("r12:  ",self.rasstoyanie12)
        self.rasstoyanie13 = 0
        for i,e in enumerate(self.SK1_short[0]):
            if e != self.SK1_short[2][i]:
                self.rasstoyanie13 += 1
        print("r13:  ",self.rasstoyanie13)

        self.rasstoyanie21 = 0
        for i,e in enumerate(self.SK2_short[1]):
            if e != self.SK2_short[0][i]:
                self.rasstoyanie21 += 1
        print("r21:  ",self.rasstoyanie21)
        self.rasstoyanie23 = 0
        for i,e in enumerate(self.SK2_short[1]):
            if e != self.SK2_short[2][i]:
                self.rasstoyanie23 += 1
        print("r23:  ",self.rasstoyanie23)

        self.rasstoyanie31 = 0
        for i,e in enumerate(self.SK3_short[2]):
            if e != self.SK3_short[0][i]:
                self.rasstoyanie31 += 1
        print("r31:  ",self.rasstoyanie31)
        self.rasstoyanie32 = 0
        for i,e in enumerate(self.SK3_short[2]):
            if e != self.SK3_short[1][i]:
                self.rasstoyanie32 += 1
        print("r32:  ",self.rasstoyanie32)
        
        self.r12.setText(str(self.rasstoyanie12))
        self.r13.setText(str(self.rasstoyanie13))
        self.r21.setText(str(self.rasstoyanie21))
        self.r23.setText(str(self.rasstoyanie23))
        self.r31.setText(str(self.rasstoyanie31))
        self.r32.setText(str(self.rasstoyanie32))
        
        self.sktextout.setText(str( self.pkrf1_strout ))

        KFE12_Shennon, KFE12_Kulbak = cnt_kfe(self.rasstoyanie12, self.SK1_short[0], self.SK1_short[1])
        KFE13_Shennon, KFE13_Kulbak = cnt_kfe(self.rasstoyanie13, self.SK1_short[0], self.SK1_short[2])
        bestkfe1, bestrad1 = bestkferad(KFE12_Shennon, KFE13_Shennon, min(self.rasstoyanie12, self.rasstoyanie13))

        print("1 KFE",bestkfe1, bestrad1,sep="\n")

        KFE21_Shennon, KFE21_Kulbak = cnt_kfe(self.rasstoyanie21, self.SK2_short[1], self.SK2_short[0])
        KFE23_Shennon, KFE23_Kulbak = cnt_kfe(self.rasstoyanie23, self.SK2_short[1], self.SK2_short[2])
        bestkfe2, bestrad2 = bestkferad(KFE21_Shennon, KFE23_Shennon, min(self.rasstoyanie21, self.rasstoyanie23))
        
        print("2 KFE",bestkfe2, bestrad2,sep="\n")

        KFE31_Shennon, KFE31_Kulbak = cnt_kfe(self.rasstoyanie31, self.SK3_short[2], self.SK2_short[0])
        KFE32_Shennon, KFE32_Kulbak = cnt_kfe(self.rasstoyanie32, self.SK3_short[2], self.SK2_short[1])
        bestkfe3, bestrad3 = bestkferad(KFE31_Shennon, KFE32_Shennon, min(self.rasstoyanie31, self.rasstoyanie32))
        
        print("3 KFE",bestkfe3, bestrad3,sep="\n")



#        print(KFE12_Shennon, KFE12_Kulbak,sep="\n")

        
        
        
def cnt_kfe(dist, sk_1, sk_2):
    k1=[0]*dist
    k2=[0]*dist
    k3=[0]*dist
    k4=[0]*dist
    alpha=[0]*dist
    beta=[0]*dist
    D1=[0]*dist
    D2=[0]*dist
    KFE_Kulbak=[0]*dist
    KFE_Shennon=[0]*dist
    for i in range(dist):
        for j in range(100):
            if sk_1[j]<=i:
                k1[i]+=1
            else: k2[i]+=1
            if sk_2[j]<=i:
                k3[i]+=1
            else: k4[i]+=1
        alpha[i]=k2[i]/100
        beta[i]=k3[i]/100
        D1[i]=k1[i]/100
        D2[i]=k4[i]/100
        if ((k1[i]!=0) and (k2[i]!=0) and (k3[i]!=0) and (k4[i]!=0)):
            KFE_Shennon[i]=1+1/2*(k1[i]/(k1[i]+k3[i])*np.log2(k1[i]/(k1[i]+k3[i])) + k2[i]/(k2[i]+k4[i])*np.log2(k2[i]/(k2[i]+k4[i])) + k3[i]/(k1[i]+k3[i])*np.log2(k3[i]/(k1[i]+k3[i])) + k4[i]/(k2[i]+k4[i])*np.log2(k4[i]/(k2[i]+k4[i])))
        else:
            KFE_Shennon[i]=0
        KFE_Kulbak[i]=1/100*np.log2((200+(10**(-5))-k2[i]-k3[i])/(k2[i]+k3[i]+(10**(-5))))*(100-k2[i]-k3[i])
    return (KFE_Shennon, KFE_Kulbak)

def bestkferad(KFE1, KFE2, dist):
    maxkfe=0
    bestrad=0
    for i in range(dist):
        if (KFE1[i]+KFE2[i]>maxkfe):
            maxkfe=KFE1[i]+KFE2[i]
            bestrad=i
    return (maxkfe, bestrad)



app = QApplication(sys.argv)
window = MainWindow()
#window.setMinimumSize(810, 810)
window.show()
sys.exit(app.exec())


