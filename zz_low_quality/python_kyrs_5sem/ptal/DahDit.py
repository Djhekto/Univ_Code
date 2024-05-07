#Написать класс morse("строка"), экземпляр которого переводит арифметические выражения в морзянку! В выражении «+» — это точка, «-» — тире, а «~» — промежуток между буквами 
#Параметр — строка, состоящая либо из символов, либо из слов.
#Строка состоит из слов, если в ней есть хотя бы один пробел
#Если в строке три элемента, они задают точку, точку на конце передаваемой буквы (традиционно обозначается другим слогом) и тире
#Два элемента задают точку (она же точка на конце буквы) и тире
#Если элемента четыре, четвёртый — это то, что выводится в конце сообщения

#По умолчанию:
#Если параметров нет, это слова "di", "dit" и "dah".
#Если параметры — слова: в конце сообщения выводится ".", разделители при выводе: пробел между сигналами и ", " между буквами.
#Если параметры — символы: непуст только разделитель между буквами (это пробел).

global ii


class morse(object):
    otvet = ""
    def __init__(self, buffer=""):
        self.buffer = buffer
        self.four = ""
        self.kostil=0
        #
        if buffer == "":
            buffer = self.buffer ="di dit dah"
        self.isslova = 0 
        if self.buffer.find(" ")!=-1:
            self.isslova = 1
        #
        if self.buffer[-1]==" ":
            self.kostil = 1
        #
        if self.isslova == 1:
            buffer = self.buffer.split()
            self.one = buffer[0]
            self.two = buffer[1]
            self.tri = buffer[2]
#            print(self.one,self.two,self.tri)
            if len(buffer)==4:
                self.four = buffer[3]
#---------------------------------------------------------------------------------------------------------
        if self.isslova == 0:
            self.logic = 0
            if any(ele.isalpha() for ele in buffer):        self.logic = 1
            if any(ele.isdecimal() for ele in buffer):      self.logic = 1
            if any(ele=="^" for ele in buffer):             self.logic = 1
            if any(ele==":" for ele in buffer):             self.logic = 1
            if any(ele=="@" for ele in buffer):             self.logic = 1
            if any(ele=="_" for ele in buffer):             self.logic = 1
            if len(buffer)==2:
                self.logic1 = 2
                self.one = buffer[0]
                self.two = buffer[1]
            if len(buffer)==3:
                self.logic1 = 3
                self.one = buffer[0]
                self.two = buffer[1]
                self.tri = buffer[2]
            if len(buffer)>=4:
                self.logic1 = 4
                self.one = buffer[0]
                self.two = buffer[1]
                self.tri = buffer[2]
                self.four = buffer[3:]
#========================================================================================================            
    def __neg__(self):#unary -
        self.otvet = "-" + self.otvet
        return self
    def __pos__(self):#unary +
        self.otvet = "." + self.otvet
        return self
    def __invert__(self):#unary ~
        if self.isslova==0:
            self.otvet = " " + self.otvet
        if self.isslova==1:
            self.otvet = ", " +self.otvet
        return self
#========================================================================================================
    def __str__(self):
        if self.isslova == 0:#символы
            if self.logic == 0:
                return self.otvet+self.four
#--------------------------------------------------------------------------------------------------------
            if self.logic1==2:
                self.otvet = self.otvet+" "
                self.otvet = self.otvet.replace(".",self.one) 
                self.otvet = self.otvet.replace("-",self.two)
                self.otvet = self.otvet.rstrip()#bag bil     
            if self.logic1>=3:
#                print(self.otvet)
                if self.otvet[-1]==".": self.otvet = self.otvet[:-1] + self.two
                self.otvet = self.otvet.replace(". ",self.two+" ")
                self.otvet = self.otvet.replace(".",self.one)
                self.otvet = self.otvet.replace("- ",self.tri+" ")#bag bil
                self.otvet = self.otvet.replace("-",self.tri)
                #self.otvet = self.otvet.rstrip()#bag bil    
                self.otvet = self.otvet+self.four
                #self.otvet = self.otvet+" "+self.four
                self.otvet = self.otvet.rstrip()   
            return self.otvet
#--------------------------------------------------------------------------------------------------------
        self.otvet = self.otvet+" "#bag bil
        #слова
        # . -> one
        # .,|." " -> two
        # - -> tri
        self.otvet = self.otvet.replace(". ",self.two+" ")
        self.otvet = self.otvet.replace(".,",self.two+",")
        self.otvet = self.otvet.replace(".",self.one+" ")
        self.otvet = self.otvet.replace("-,",self.tri+",")#bag bil
        self.otvet = self.otvet.replace("- ",self.tri)#bag bil
        self.otvet = self.otvet.replace("-",self.tri+" ")
        self.otvet = self.otvet.rstrip()#bag bil
        if self.four == "":
            if self.kostil==0:
                self.otvet = self.otvet+"."
        return self.otvet+self.four

