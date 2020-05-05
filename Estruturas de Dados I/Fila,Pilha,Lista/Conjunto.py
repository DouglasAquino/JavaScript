class Conjunto():
    def __init__(self,*valores):
        self.__conj=[]
        for i in range(11):
            if i in valores:
                self.__conj.append(True)
            else:
                self.__conj.append(False)
    def show(self):
        for i,j in enumerate (self.__conj):
            if j:
                print(i)
    def uniao(self,conjunto2):
        
        print(conjunto2)
        
        
        
        

        
       
