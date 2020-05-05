class NoA():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo
   
    def getInfo(self):
        return self.info
    
    def getProx(self):
        return self.prox
    
    def setInfo(self, valor):
        self.info=valor
      
    def setProx(self,proximo):
        self.prox=proximo

class NoB():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo
   
    def getInfo(self):
        return self.info
    
    def getProx(self):
        return self.prox
    
    def setInfo(self, valor):
        self.info=valor
      
    def setProx(self,proximo):
        self.prox=proximo


class BaralhoA():
    def __init__(self):
        self.prim=None
        self.ult=None
        self.quant=0
        
    def inserirTopo(self,valor):
        newNo = NoA(valor,None)
        if self.quant==0:
            self.prim=self.ult=newNo

        else:
            newNo.setProx(self.prim)
            self.prim=newNo

        self.quant+=1

    def inserirBase(self,valor):
        newNo = NoA(valor,None)
        if self.quant==0:
            self.prim=self.ult=newNo

        else:
            self.ult.setProx(newNo)
            self.ult=newNo
            

        self.quant+=1

    def removerTopo(self):
        if self.quant==1:
            self.prim=self.ult=None

        else:
            self.prim=self.prim.getProx()

        self.quant-=1
        

    def show(self):
        aux=self.prim
        
        while aux!=None:
            print(aux.getInfo())
            aux=aux.getProx()
    def getPrim(self):
        return self.prim.getInfo()

class BaralhoB():
    def __init__(self):
        self.prim=None
        self.ult=None
        self.quant=0
        
    def inserirTopo(self,valor):
        newNo = NoB(valor,None)
        if self.quant==0:
            self.prim=self.ult=newNo

        else:
            newNo.setProx(self.prim)
            self.prim=newNo

        self.quant+=1

    def inserirBase(self,valor):
        newNo = NoB(valor,None)
        if self.quant==0:
            self.prim=self.ult=newNo

        else:
            self.ult.setProx(newNo)
            self.ult=newNo
        self.quant+=1

    def removerTopo(self):
        if self.quant==1:
            self.prim=self.ult=None

        else:
            self.prim=self.prim.getProx()

        self.quant-=1
        

    def show(self):
        aux=self.prim
        
        while aux!=None:
            print(aux.getInfo())
            aux=aux.getProx()

    def getPrim(self):
        return self.prim.getInfo()


        
    
    
