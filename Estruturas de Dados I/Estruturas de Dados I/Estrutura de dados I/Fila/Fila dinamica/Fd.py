class No():
    def __init__(self,valor,proximo):
        self.inf = valor
        self.prox = proximo
class Fd():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def inserir(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1
        
    def remover(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
        
    def show(self):
        aux=self.prim
        while aux != None:
            print(aux.inf)
            aux=aux.prox
            
    def estarVazia(self):
        self.quant==0
        
