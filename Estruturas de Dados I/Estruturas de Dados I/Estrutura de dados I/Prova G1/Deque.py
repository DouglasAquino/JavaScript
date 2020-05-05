class No():
    def __init__(self,valor,proximo):
        self.inf = valor
        self.prox = proximo
class Deque():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def addBase(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1
        
    def removerBase(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
        
    def getTopo(self):
        aux=self.prim
        while aux != None:
            print(aux.inf)
            break
            
            
    def addTopo(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1

    def removerTopo(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox != self.ult:
                aux=aux.prox
            self.ult=aux
            aux.prox=None
        self.quant-=1



