from PIL import Image
import numpy as np

import sys
from PyQt6.QtGui import QPixmap, QAction, QColor, QPainter, QTransform
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QStackedLayout,QLineEdit, QGridLayout, QLabel,QTableWidget, QTableWidgetItem, QFileDialog,QTableView
from PyQt6.QtCore import Qt,QAbstractTableModel

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from torch import true_divide


class MainWindow(QMainWindow):
    def __init__(self,myname):
        super().__init__()
        self.myname = myname
        self.IMAGESIZE = 90
        self.setWindowTitle("ВЫПОЛНЕНИЕ ЗАДАЧИ ПРИ ОПТИМИЗАЦИИ ПАРАМЕТРОВ")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QGridLayout()
        
        label = QLabel("Картинки:")
        self.layout.addWidget(label,0, 0)
        label = QLabel("Картинки для бинарной матрицы:")
        self.layout.addWidget(label,1, 0)
        label = QLabel("Параметры:  ")
        self.layout.addWidget(label,2, 0)
        label = QLabel("Графики KFE:")
        self.layout.addWidget(label,3, 0)
        self.button = QPushButton("Посчитать")
        self.button.clicked.connect(self.main_calculation)
        self.layout.addWidget(self.button ,4, 0)

        self.picture_out1bin = QLabel()
        #self.picture_out1bin.setScaledContents(True);
        self.layout.addWidget(self.picture_out1bin,1, 1)
        self.picture_out2bin = QLabel()
        #self.picture_out2bin.setScaledContents(True);
        self.layout.addWidget(self.picture_out2bin,1, 2)
        self.picture_out3bin = QLabel()
        #self.picture_out3bin.setScaledContents(True);
        self.layout.addWidget(self.picture_out3bin,1, 3)
        self.picture_out4bin = QLabel()
        #self.picture_out4bin.setScaledContents(True);
        self.layout.addWidget(self.picture_out4bin,1, 4)

        self.txt_out1par = QLabel()
        self.str_out1par = ""
        self.layout.addWidget(self.txt_out1par,2, 1)
        self.txt_out2par = QLabel()
        self.str_out2par = ""
        self.layout.addWidget(self.txt_out2par,2, 2)
        self.txt_out3par = QLabel()
        self.str_out3par = ""
        self.layout.addWidget(self.txt_out3par,2, 3)
        self.txt_out4par = QLabel()
        self.str_out4par = ""
        self.layout.addWidget(self.txt_out4par,2, 4)
                        
        self.holdmatrixobjectsforme = []
        for j in range(1,5):
                label = QLabel()
                pixmap = QPixmap(f'{j}.png')
                image_1 = Image.open(f'{j}.png')
                image_1 = image_1.convert("L")
                matrix1 = np.asarray(np.array(image_1))
                self.holdmatrixobjectsforme.append(matrix1)
                label.setPixmap(pixmap)
                self.layout.addWidget(label,0, j)
        
        print(self.holdmatrixobjectsforme)

        central_widget.setLayout(self.layout)

   
    def main_calculation(self):
        np.set_printoptions(threshold=np.inf)
        bestkfe = -1
        last_cfe = 0
        for delta in range(60,62,100):
            weshouldbreakthings = False
            weshouldconsiderbreaking = False
            
            self.matrixbin1 = self.holdmatrixobjectsforme[0]
            for i,e in enumerate(self.holdmatrixobjectsforme[0]):
                #print(e)
                avrg = np.mean(e)
                avrg1= avrg - delta
                #print(avrg, avrg1)
                for ii,ee in enumerate(e):
                    if ee <= avrg and ee >= avrg1:
                        self.matrixbin1[i][ii] = 1
                    else:
                        self.matrixbin1[i][ii] = 0

            self.matrixbin2 = self.holdmatrixobjectsforme[1]
            for i,e in enumerate(self.holdmatrixobjectsforme[1]):
                avrg = np.mean(e)
                avrg1= avrg - delta
                for ii,ee in enumerate(e):
                    if ee <= avrg and ee >= avrg1:
                        self.matrixbin2[i][ii] = 1
                    else:
                        self.matrixbin2[i][ii] = 0

            self.matrixbin3 = self.holdmatrixobjectsforme[2]
            for i,e in enumerate(self.holdmatrixobjectsforme[2]):
                avrg = np.mean(e)
                avrg1= avrg - delta
                for ii,ee in enumerate(e):
                    if ee <= avrg and ee >= avrg1:
                        self.matrixbin3[i][ii] = 1
                    else:
                        self.matrixbin3[i][ii] = 0

            self.matrixbin4 = self.holdmatrixobjectsforme[3]
            for i,e in enumerate(self.holdmatrixobjectsforme[3]):
                avrg = np.mean(e)
                avrg1= avrg - delta
                for ii,ee in enumerate(e):
                    if ee <= avrg and ee >= avrg1:
                        self.matrixbin4[i][ii] = 1
                    else:
                        self.matrixbin4[i][ii] = 0

            for ro_1 in range(50,56,100):
                nro_1 = ro_1/100
                if weshouldbreakthings:
                    break

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

                for ro_2 in range(50,56,100):
                    nro_2 = ro_2/100
                    if weshouldbreakthings:
                        break

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

                    for ro_3 in range(50,56,100):
                        nro_3 = ro_3/100
                        if weshouldbreakthings:
                            break

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

                        for ro_4 in range(50,56,100):
                            nro_4 = ro_4/100
                            if ro_4>self.IMAGESIZE:
                                weshouldbreakthings = True
                                break
                            if ro_1>self.IMAGESIZE:
                                weshouldbreakthings = True
                                break
                            if ro_2>self.IMAGESIZE:
                                weshouldbreakthings = True
                                break
                            if ro_3>self.IMAGESIZE:
                                weshouldbreakthings = True
                                break
                            if weshouldbreakthings:
                                break

                            self.EV4 = []
                            for i,e in enumerate(self.matrixbin4):
                                tempcount = 0
                                for ii,ee in enumerate(e):
                                    if ee == 1:
                                        tempcount+=1
                                if tempcount>= (len(self.matrixbin4[0])*nro_4):
                                    self.EV4.append( 1 )
                                else:
                                    self.EV4.append( 0 )

                            #print(f"EV1 = {self.EV1}\nEV2 = {self.EV2}\nEV3 = {self.EV3}\nEV4 = {self.EV4}\n")
                            print(delta,ro_1,ro_2,ro_3,ro_4)

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
                            
                            list_append_me = []        
                            for i,e in enumerate(self.EV1):
                                counter_append_me = 0
                                for ee in self.matrixbin4[i]:
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
                            
                            list_append_me = []        
                            for i,e in enumerate(self.EV2):
                                counter_append_me = 0
                                for ee in self.matrixbin4[i]:
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

                            list_append_me = []        
                            for i,e in enumerate(self.EV3):
                                counter_append_me = 0
                                for ee in self.matrixbin4[i]:
                                    if e!=ee:
                                        counter_append_me += 1
                                list_append_me.append(counter_append_me)
                            self.SK3_short.append(list_append_me)
                                                    
                            #print(f"Кодовое расстояние между EV3 и бинарными матрицами 1,2,3 соответственно: \n{self.SK3_short[0]}\n{self.SK3_short[1]}\n{self.SK3_short[2]}")        
                            #self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV3 и бинарными матрицами 1,2,3 соответственно: \n{self.SK3_short[0]}\n{self.SK3_short[1]}\n{self.SK3_short[2]}"+"\n"

                            self.SK4_short     = []
                            self.pkrf1_strout = ""

                            list_append_me = []        
                            for i,e in enumerate(self.EV4):
                                counter_append_me = 0
                                for ee in self.matrixbin1[i]:
                                    if e!=ee:
                                        counter_append_me += 1
                                list_append_me.append(counter_append_me)
                            self.SK4_short.append(list_append_me)

                            list_append_me = []        
                            for i,e in enumerate(self.EV4):
                                counter_append_me = 0
                                for ee in self.matrixbin2[i]:
                                    if e!=ee:
                                        counter_append_me += 1
                                list_append_me.append(counter_append_me)
                            self.SK4_short.append(list_append_me)
                            
                            list_append_me = []        
                            for i,e in enumerate(self.EV4):
                                counter_append_me = 0
                                for ee in self.matrixbin3[i]:
                                    if e!=ee:
                                        counter_append_me += 1
                                list_append_me.append(counter_append_me)
                            self.SK4_short.append(list_append_me)
                            
                            list_append_me = []        
                            for i,e in enumerate(self.EV4):
                                counter_append_me = 0
                                for ee in self.matrixbin4[i]:
                                    if e!=ee:
                                        counter_append_me += 1
                                list_append_me.append(counter_append_me)
                            self.SK4_short.append(list_append_me) 
                            
                            #print(f"Кодовое расстояние между EV1 и бинарными матрицами 1,2,3 соответственно: \n{self.SK1_short[0]}\n{self.SK1_short[1]}\n{self.SK1_short[2]}")        
                            #self.pkrf1_strout =  self.pkrf1_strout+f"Кодовое расстояние между EV1 и бинарными матрицами 1,2,3 соответственно: \n{self.SK1_short[0]}\n{self.SK1_short[1]}\n{self.SK1_short[2]}"+"\n"
                            

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
                            #self.rasstoyanie32 = 0
                            #for i,e in enumerate(self.SK3_short[2]):
                            #    if e != self.SK3_short[1][i]:
                            #        self.rasstoyanie32 += 1
                            #print("r32:  ",self.rasstoyanie32)
                            
                            self.rasstoyanie34 = 0
                            for i,e in enumerate(self.SK3_short[2]):
                                if e != self.SK3_short[3][i]:
                                    self.rasstoyanie34 += 1
                            
                            self.rasstoyanie41 = 0
                            for i,e in enumerate(self.SK4_short[3]):
                                if e != self.SK4_short[0][i]:
                                    self.rasstoyanie41 += 1

                            
                            #self.sktextout.setText(str( self.pkrf1_strout ))

                            KFE12_Shennon, KFE12_Kulbak = cnt_kfe(self.rasstoyanie12, self.SK1_short[0], self.SK1_short[1],self.IMAGESIZE)
                            #KFE13_Shennon, KFE13_Kulbak = cnt_kfe(self.rasstoyanie13, self.SK1_short[0], self.SK1_short[2],self.IMAGESIZE)
                            #bestkfe1, bestrad1 = bestkferad(KFE12_Shennon, KFE13_Shennon, min(self.rasstoyanie12, self.rasstoyanie13))
                            bestkfe1, bestrad1 = bestkferad(KFE12_Shennon , KFE12_Shennon , min( self.rasstoyanie12,  self.rasstoyanie12))
                            #print("1 KFE",bestkfe1, bestrad1,sep="\n")

                            #KFE21_Shennon, KFE21_Kulbak = cnt_kfe(self.rasstoyanie21, self.SK2_short[1], self.SK2_short[0],self.IMAGESIZE)
                            KFE23_Shennon, KFE23_Kulbak = cnt_kfe(self.rasstoyanie23, self.SK2_short[1], self.SK2_short[2],self.IMAGESIZE)
                            #bestkfe2, bestrad2 = bestkferad(KFE21_Shennon, KFE23_Shennon, min(self.rasstoyanie21, self.rasstoyanie23))
                            bestkfe2, bestrad2 = bestkferad(KFE23_Shennon, KFE23_Shennon, min(self.rasstoyanie23, self.rasstoyanie23))
                            #print("2 KFE",bestkfe2, bestrad2,sep="\n")

                            #KFE31_Shennon, KFE31_Kulbak = cnt_kfe(self.rasstoyanie31, self.SK3_short[2], self.SK3_short[0],self.IMAGESIZE)
                            #KFE32_Shennon, KFE32_Kulbak = cnt_kfe(self.rasstoyanie32, self.SK3_short[2], self.SK3_short[1],self.IMAGESIZE)
                            #bestkfe3, bestrad3 = bestkferad(KFE31_Shennon, KFE32_Shennon, min(self.rasstoyanie31, self.rasstoyanie32))
                            KFE34_Shennon, KFE34_Kulbak = cnt_kfe(self.rasstoyanie34, self.SK3_short[2], self.SK3_short[3],self.IMAGESIZE)
                            bestkfe3, bestrad3 = bestkferad(KFE34_Shennon , KFE34_Shennon , min( self.rasstoyanie34,  self.rasstoyanie34))
                            #print("3 KFE",bestkfe3, bestrad3,sep="\n")
                            
                            KFE41_Shennon, KFE41_Kulbak = cnt_kfe(self.rasstoyanie41, self.SK4_short[3], self.SK4_short[0],self.IMAGESIZE)
                            bestkfe4, bestrad4 = bestkferad(KFE41_Shennon , KFE41_Shennon , min( self.rasstoyanie41,  self.rasstoyanie41))
                            
                            boolfirsteverloop = False
                            cur_kfe=bestkfe1+bestkfe2+bestkfe3+bestkfe4
                            print(cur_kfe)
                            if cur_kfe == last_cfe:
                                print("brr")
                                if   weshouldconsiderbreaking:
                                    #weshouldbreakthings = True
                                    print("br")
                                    break
                                weshouldconsiderbreaking = True
                            else:
                                weshouldconsiderbreaking = False
                            last_cfe = cur_kfe
                            if (cur_kfe>bestkfe):
                                bestkfe=cur_kfe
                                sbestdelta=delta
                                sbestro1=ro_1
                                sbestro2=ro_2
                                sbestro3=ro_3
                                sbestro4=ro_4
                                BESTKFE12_Shennon, BESTKFE12_Kulbak = KFE12_Shennon, KFE12_Kulbak
                                BESTKFE23_Shennon, BESTKFE23_Kulbak = KFE23_Shennon, KFE23_Kulbak
                                BESTKFE34_Shennon, BESTKFE34_Kulbak = KFE34_Shennon, KFE34_Kulbak
                                BESTKFE41_Shennon, BESTKFE41_Kulbak = KFE41_Shennon, KFE41_Kulbak
                                #BESTKFE13_Shennon, BESTKFE13_Kulbak = KFE13_Shennon, KFE13_Kulbak                            
                                #BESTKFE21_Shennon, BESTKFE21_Kulbak = KFE21_Shennon, KFE21_Kulbak
                                #BESTKFE31_Shennon, BESTKFE31_Kulbak = KFE31_Shennon, KFE31_Kulbak
                                #BESTKFE32_Shennon, BESTKFE32_Kulbak = KFE32_Shennon, KFE32_Kulbak

        delta=sbestdelta
        ro1=sbestro1/100
        ro2=sbestro2/100
        ro3=sbestro3/100
        ro4=sbestro4/100
        print("Конец первого этапа оптимизации")
        print(f"Лучшее значение дельта = {delta}\n")
        print(f"Лучшее значение ро 1 {ro1}\n")
        print(f"Лучшее значение ро 2 {ro2}\n")
        print(f"Лучшее значение ро 3 {ro3}\n")
        print(f"Лучшее значение ро 4 {ro4}\n")
        self.str_out1par = self.str_out1par+f"дельта = {delta}\nро1 = {ro1}\n"
        self.txt_out1par.setText(self.str_out1par)
        self.str_out2par = self.str_out2par+f"дельта = {delta}\nро2 = {ro2}\n"
        self.txt_out2par.setText(self.str_out2par)
        self.str_out3par = self.str_out3par+f"дельта = {delta}\nро3 = {ro3}\n"
        self.txt_out3par.setText(self.str_out3par)
        self.str_out4par = self.str_out4par+f"дельта = {delta}\nро4 = {ro4}\n"
        self.txt_out4par.setText(self.str_out4par)
        print(f"Лучшее значение суммы кфе Шеннона KFE {bestkfe}\n")
        #print(f" оно получено из:\n BESTKFE12_Shennon = {BESTKFE12_Shennon} BESTKFE13_Shennon = {BESTKFE13_Shennon}\n")
        #print(f" BESTKFE21_Shennon = {BESTKFE21_Shennon} BESTKFE23_Shennon = {BESTKFE23_Shennon}\n")
        #print(f" BESTKFE31_Shennon = {BESTKFE31_Shennon} BESTKFE32_Shennon = {BESTKFE32_Shennon}\n")
        print(f"EV1 = {self.EV1}\nEV2 = {self.EV2}\nEV3 = {self.EV3}\nEV4 = {self.EV4}\n")
        
        
        pixmap2 = QPixmap(self.IMAGESIZE, self.IMAGESIZE)
        painter = QPainter(pixmap2)
        for i in range(self.IMAGESIZE):
            for j in range(self.IMAGESIZE):
                color2 = QColor(0,0,0)
                if  self.matrixbin1[i][j] == 0:
                    color2 = QColor(255, 255, 255)
                painter.setPen(color2)
                painter.setBrush(QColor(255, 255, 255))
                painter.drawRect(j, i, 1, 1)
        painter.end()
        pixmap2.save("output.png")
        self.picture_out1bin.setPixmap(pixmap2)  
           
        pixmap2 = QPixmap(self.IMAGESIZE, self.IMAGESIZE)
        painter = QPainter(pixmap2)
        for i in range(self.IMAGESIZE):
            for j in range(self.IMAGESIZE):
                color2 = QColor(0,0,0)
                if  self.matrixbin2[i][j] == 0:
                    color2 = QColor(255, 255, 255)
                painter.setPen(color2)
                painter.setBrush(QColor(255, 255, 255))
                painter.drawRect(j, i, 1, 1)
        painter.end()
        pixmap2.save("output.png")
        self.picture_out2bin.setPixmap(pixmap2)        
           
        pixmap2 = QPixmap(self.IMAGESIZE, self.IMAGESIZE)
        painter = QPainter(pixmap2)
        for i in range(self.IMAGESIZE):
            for j in range(self.IMAGESIZE):
                color2 = QColor(0,0,0)
                if  self.matrixbin3[i][j] == 0:
                    color2 = QColor(255, 255, 255)
                painter.setPen(color2)
                painter.setBrush(QColor(255, 255, 255))
                painter.drawRect(j, i, 1, 1)
        painter.end()
        pixmap2.save("output.png")
        self.picture_out3bin.setPixmap(pixmap2)        
           
        pixmap2 = QPixmap(self.IMAGESIZE, self.IMAGESIZE)
        painter = QPainter(pixmap2)
        for i in range(self.IMAGESIZE):
            for j in range(self.IMAGESIZE):
                color2 = QColor(0,0,0)
                if  self.matrixbin4[i][j] == 0:
                    color2 = QColor(255, 255, 255)
                painter.setPen(color2)
                painter.setBrush(QColor(255, 255, 255))
                painter.drawRect(j, i, 1, 1)
        painter.end()
        pixmap2.save("output.png")
        self.picture_out4bin.setPixmap(pixmap2)  
        
        #self.figure = Figure()
        #self.canvas = FigureCanvas(self.figure)
        #self.axis = self.figure.add_subplot(111)
        #self.layout.addWidget(self.canvas,3, 1)
        
        fig1, ax1 = plt.subplots()
        ax1.plot(BESTKFE12_Shennon,label=f'Для delta = {delta} ro_1 = {ro1}')
        plt.ylim(0, 1)
        plt.legend()
        plt.title("KFE12")
        fig1.savefig('111.png')  
        canvas = FigureCanvas(fig1)   
        self.layout.addWidget(canvas,3, 1)

        fig1, ax1 = plt.subplots()
        ax1.plot(BESTKFE23_Shennon,label=f'Для delta = {delta} ro_2 = {ro2}')
        plt.ylim(0, 1)
        plt.legend()
        plt.title("KFE23")
        fig1.savefig('222.png')  
        canvas = FigureCanvas(fig1)   
        self.layout.addWidget(canvas,3, 2)

        fig1, ax1 = plt.subplots()
        ax1.plot(BESTKFE34_Shennon,label=f'Для delta = {delta} ro_3 = {ro3}')
        plt.ylim(0, 1)
        plt.legend()
        plt.title("KFE34")
        fig1.savefig('333.png')  
        canvas = FigureCanvas(fig1)   
        self.layout.addWidget(canvas,3, 3)

        fig1, ax1 = plt.subplots()
        ax1.plot(BESTKFE41_Shennon,label=f'Для delta = {delta} ro_4 = {ro4}')
        plt.ylim(0, 1)
        plt.legend()
        plt.title("KFE41")
        fig1.savefig('444.png')  
        canvas = FigureCanvas(fig1)   
        self.layout.addWidget(canvas,3, 4)
        
        print(self.rasstoyanie12,self.rasstoyanie21,self.rasstoyanie31,self.rasstoyanie41)
        r1s=vychislkfe_class(self.rasstoyanie12, self.rasstoyanie21, self.SK1_short[0], self.SK1_short[1], self.SK2_short[1], self.SK2_short[0], 1, 2, 3,BESTKFE12_Shennon,BESTKFE23_Shennon)
        r2s=vychislkfe_class(self.rasstoyanie21, self.rasstoyanie12, self.SK2_short[1], self.SK2_short[0], self.SK1_short[0], self.SK1_short[1], 2, 1, 3,BESTKFE23_Shennon,BESTKFE34_Shennon)
        r3s=vychislkfe_class(self.rasstoyanie31, self.rasstoyanie12, self.SK3_short[2], self.SK3_short[0], self.SK1_short[0], self.SK1_short[1], 3, 1, 2,BESTKFE34_Shennon,BESTKFE41_Shennon)
        r4s=vychislkfe_class(self.rasstoyanie41, self.rasstoyanie12, self.SK4_short[3], self.SK4_short[0], self.SK1_short[0], self.SK1_short[1], 4, 1, 2,BESTKFE41_Shennon,BESTKFE12_Shennon)
        

        import random
        trials=100
        correct=0
        for t in range(trials):
            fromcl=random.choice([1,2,3,4])
            real=random.randrange(0,90)
            pred=0
            if t%10==0: print("Выбрана реализация",real,"из класса", fromcl)
            if fromcl==1:
                test_string=self.matrixbin1[real]#self.IMAGESIZE
            if fromcl==2:
                test_string=self.matrixbin2[real]
            if fromcl==3:
                test_string=self.matrixbin3[real]
            if fromcl==4:
                test_string=self.matrixbin4[real]
            d1=0
            d2=0
            d3=0
            d4=0
            for j in range(80):
                if test_string[j]!=self.EV1[j]:
                    d1+=1
                if test_string[j]!=self.EV2[j]:
                    d2+=1
                if test_string[j]!=self.EV3[j]:
                    d3+=1
                if test_string[j]!=self.EV4[j]:
                    d4+=1
            try:
                mu1=1-d1/r1s
            except:
                mu1=1-d1/1
            try:
                mu2=1-d2/r2s
            except:
                mu2=1-d2/1
            try:
                mu3=1-d3/r3s
            except:
                mu3=1-d3/1
            try:
                mu4=1-d4/r4s
            except:
                mu4=1-d4/1
            if t%10==0: print("Функция принадлежности 1 классу",mu1)
            if t%10==0: print("Функция принадлежности 2 классу",mu2)
            if t%10==0: print("Функция принадлежности 3 классу",mu3)
            if t%10==0: print("Функция принадлежности 4 классу",mu4)
            c=0.5
            mx=max(mu1,mu2,mu3,mu4)
            cont=0
            if mx==mu1: cont+=1
            if mx==mu2: cont+=1
            if mx==mu3: cont+=1
            if mx==mu4: cont+=1
            #if ((cont>1) or max(mu1,mu2,mu3,mu4)<=0) and (t%10==0): 
            #    print("Объект не принадлежит ни одному классу")
            if False: pass
            #elif ((mu1>mu2) and (mu1>mu3)):
            elif mx==mu1:
                pred=1
                if t%10==0: print("Объект принадлежит 1 классу")
            #elif ((mu2>mu1) and (mu2>mu3)):
            elif mx==mu2:
                pred=2
                if t%10==0: print("Объект принадлежит 2 классу")
            #elif ((mu3>mu1) and (mu3>mu1)):
            elif mx==mu3:
                pred=3
                if t%10==0: print("Объект принадлежит 3 классу")
            elif mx==mu4:
                pred=4
                if t%10==0: print("Объект принадлежит 4 классу")
            #if t%10==0: print('Реализация')
            test_8bit=[]
            for i in range(90):
                test_8bit.append(255-test_string[i]*255)
            test_matr=[]
            for i in range(10):
                test_matr.append(test_8bit)
            etimg3 = Image.fromarray(np.array(test_matr).astype(np.uint8))
            #if t%10==0: display(etimg3)
            #if t%10==0: 
            #    for j in range(0,90,10):
            #        print(test_string[j],"...",end="")
            if pred==fromcl: 
                correct+=1
            if t%10==0: print()
            if t%10==0: print("==========================")
        print("Успешно предсказано",correct,"из", trials, ", доля верных =", correct/trials)
        

        
        
        

def vychislkfe_class(dist1, dist2, sk1_1, sk1_2, sk2_1, sk2_2, our, another1, another2,kfe1,kfe2):
  #print("Исследуемый класс:", our, ", чужой класс:", another1)
  k1=[dist1]
  k2=[dist1]
  k3=[dist1]
  k4=[dist1]
  alpha=[dist1]
  beta=[dist1]
  D1=[dist1]
  D2=[dist1]
  #KFE1_Kulbak=[dist1]
  KFE1_Shennon=kfe1
  orange=[dist1]
  blue=[dist1]
  for i in range(dist1):
    for j in range(90):
      if sk1_1[j]<=i:
        k1[i]+=1
      else: k2[i]+=1
      if sk1_2[j]<=i:
        k3[i]+=1
      else: k4[i]+=1
    alpha[i]=k2[i]/90
    beta[i]=k3[i]/90
    D1[i]=k1[i]/90
    D2[i]=k4[i]/90
    #if ((k1[i]!=0) and (k2[i]!=0) and (k3[i]!=0) and (k4[i]!=0)):
    #try:
    #  KFE1_Shennon[i]=1+1/2*(k1[i]/(k1[i]+k3[i])*np.log2(k1[i]/(k1[i]+k3[i])) + k2[i]/(k2[i]+k4[i])*np.log2(k2[i]/(k2[i]+k4[i])) + k3[i]/(k1[i]+k3[i])*np.log2(k3[i]/(k1[i]+k3[i])) + k4[i]/(k2[i]+k4[i])*np.log2(k4[i]/(k2[i]+k4[i])))
    #except:
    #else:
    #  KFE1_Shennon[i]=0
    #KFE1_Kulbak[i]=1/90*np.log2((200+(10**(-5))-k2[i]-k3[i])/(k2[i]+k3[i]+(10**(-5))))*(90-k2[i]-k3[i])
    #if (D1[i]>=0.5 and D2[i]>=0.5):
    #  orange[i]=KFE1_Kulbak[i]
    #  blue[i]=KFE1_Shennon[i]

    #print('d       Alpha    Beta     D1       D2  KFE_Shannon KFE_Kulbak')
    #for i in range(dist1):
    #    if (D1[i]<0.5 or D2[i]<0.5):
    #        print(' {0:3d}    {1:.3f}    {2:.3f}    {3:.3f}    {4:.3f}    {5:.3f}    {6:.3f}'.format(i,alpha[i],beta[i],D1[i],D2[i],KFE1_Shennon[i],KFE1_Kulbak[i]))
    #    else:
    #        print(' {0:3d}    {1:.3f}    {2:.3f}    {3:.3f}    {4:.3f}    \033[1;34m{5:.3f}\033[0m    \033[1;31m{6:.3f}\033[0m'.format(i,alpha[i],beta[i],D1[i],D2[i],KFE1_Shennon[i],KFE1_Kulbak[i]))
    #print("Исследуемый класс:", our, ", чужой класс:", another2)
    k1=[0]*dist2
    k2=[0]*dist2
    k3=[0]*dist2
    k4=[0]*dist2
    alpha=[0]*dist2
    beta=[0]*dist2
    D1=[0]*dist2
    D2=[0]*dist2
    #KFE2_Kulbak=[0]*dist2
    KFE2_Shennon=kfe2
    orange=[0]*dist2
    blue=[0]*dist2
    for i in range(dist2):
        for j in range(90):
            if sk2_1[j]<=i:
                k1[i]+=1
            else: k2[i]+=1
            if sk2_2[j]<=i:
                k3[i]+=1
            else: k4[i]+=1
        alpha[i]=k2[i]/90
        beta[i]=k3[i]/90
        D1[i]=k1[i]/90
        D2[i]=k4[i]/90
        #if ((k1[i]!=0) and (k2[i]!=0) and (k3[i]!=0) and (k4[i]!=0)):
        #    KFE2_Shennon[i]=1+1/2*(k1[i]/(k1[i]+k3[i])*np.log2(k1[i]/(k1[i]+k3[i])) + k2[i]/(k2[i]+k4[i])*np.log2(k2[i]/(k2[i]+k4[i])) + k3[i]/(k1[i]+k3[i])*np.log2(k3[i]/(k1[i]+k3[i])) + k4[i]/(k2[i]+k4[i])*np.log2(k4[i]/(k2[i]+k4[i])))
        #else:
        #    KFE2_Shennon[i]=0
        #KFE2_Kulbak[i]=1/90*np.log2((200+(10**(-5))-k2[i]-k3[i])/(k2[i]+k3[i]+(10**(-5))))*(90-k2[i]-k3[i])
        #if (D1[i]>=0.5 and D2[i]>=0.5):
        #    orange[i]=KFE2_Kulbak[i]
        #    blue[i]=KFE2_Shennon[i]
    #print('d       Alpha    Beta     D1       D2  KFE_Shannon KFE_Kulbak')
    #for i in range(dist2):
    #    if (D1[i]<0.5 or D2[i]<0.5):
    #        print(' {0:3d}    {1:.3f}    {2:.3f}    {3:.3f}    {4:.3f}    {5:.3f}    {6:.3f}'.format(i,alpha[i],beta[i],D1[i],D2[i],KFE2_Shennon[i],KFE2_Kulbak[i]))
    #    else:
    #        print(' {0:3d}    {1:.3f}    {2:.3f}    {3:.3f}    {4:.3f}    \033[1;34m{5:.3f}\033[0m    \033[1;31m{6:.3f}\033[0m'.format(i,alpha[i],beta[i],D1[i],D2[i],KFE2_Shennon[i],KFE2_Kulbak[i]))
    maxkfe_Shennon=0
    maxkfe_Kulbak=0
    optrshan=0
    optrkul=0
    print(KFE1_Shennon,dist1, dist2)
    for i in range(min(dist1, dist2)):
        #print(KFE1_Shennon[i],KFE2_Shennon[i],maxkfe_Shennon)
        try:
            if (KFE1_Shennon[i]+KFE2_Shennon[i]>maxkfe_Shennon): 
                maxkfe_Shennon=KFE1_Shennon[i]+KFE2_Shennon[i]
                optrshan=i
        except:
            pass
        #if (KFE1_Kulbak[i]+KFE2_Kulbak[i]>maxkfe_Kulbak):
        #    maxkfe_Kulbak=KFE1_Kulbak[i]+KFE2_Kulbak[i]
        #    optrkul=i
    #print("Лучший радиус по Кульбаку = ", optrkul)
    #print("Наибольшая сумма критериев по Кульбаку = ", maxkfe_Kulbak)
    #print("Лучший радиус по Шеннону = ", optrshan)
    #print("Наибольшая сумма критериев по Шеннону = ", maxkfe_Shennon)
    print(optrshan)
    return optrshan


    
def cnt_kfe(dist, sk_1, sk_2,imagesize):
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
        for j in range(imagesize):
            if sk_1[j]<=i:
                k1[i]+=1
            else: k2[i]+=1
            if sk_2[j]<=i:
                k3[i]+=1
            else: k4[i]+=1
        alpha[i]=k2[i]/imagesize
        beta[i]=k3[i]/imagesize
        D1[i]=k1[i]/imagesize
        D2[i]=k4[i]/imagesize
        if ((k1[i]!=0) and (k2[i]!=0) and (k3[i]!=0) and (k4[i]!=0)):
            KFE_Shennon[i]=1+1/2*(k1[i]/(k1[i]+k3[i])*np.log2(k1[i]/(k1[i]+k3[i])) + k2[i]/(k2[i]+k4[i])*np.log2(k2[i]/(k2[i]+k4[i])) + k3[i]/(k1[i]+k3[i])*np.log2(k3[i]/(k1[i]+k3[i])) + k4[i]/(k2[i]+k4[i])*np.log2(k4[i]/(k2[i]+k4[i])))
        else:
            KFE_Shennon[i]=0
        KFE_Kulbak[i]=1/imagesize*np.log2((200+(10**(-5))-k2[i]-k3[i])/(k2[i]+k3[i]+(10**(-5))))*(imagesize-k2[i]-k3[i])
    return (KFE_Shennon, KFE_Kulbak)

def bestkferad(KFE1, KFE2, dist):
    maxkfe=0
    bestrad=0
    for i in range(dist):
        if (KFE1[i]+KFE2[i]>maxkfe):
            maxkfe=KFE1[i]+KFE2[i]
            bestrad=i
    return (maxkfe, bestrad)

def check(list):
    return all(i == list[0] for i in list)

app = QApplication(sys.argv)
window = MainWindow("window")
window.show()
app.exec()
