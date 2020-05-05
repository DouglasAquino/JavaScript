class Frac():

    def __init__(self,num,den):#construtor da class
        self.__num = num # __ : privar o atributo 
        self.__den = den

    def getNum(self): #retorna o valor que é o num
        return self.__num
    
    def setNum(self,num):#muda o valor do num
        self.__num = num 
        
    def getDen(self):#retorna o valor que é o den
        return self.__den
    
    def setDen(self,den):#muda o valor do den
        self.__den=den
        
    def show(self):
        print(str(self.__num)+'/'+str(self.__den))
        
    def mult(self,fracao):
        self.__num = self.__num * fracao.getNum()
        self.__den = self.__den * fracao.getDen()
    
    def div(self,fracao):
        self.__num = self.__num / fracao.getNum()
        self.__den = self.__den / fracao.getDen()
        
    def soma(self,fracao):
        self.__num = self.__num + fracao.getNum()
        self.__den = self.__den + fracao.getDen()
        
    def sub(self,fracao):
        self.__num = self.__num - fracao.getNum()
        self.__den = self.__den - fracao.getDen()
      
        
