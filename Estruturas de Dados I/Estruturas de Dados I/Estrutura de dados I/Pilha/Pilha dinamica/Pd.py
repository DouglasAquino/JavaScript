class No():
    def __init__(self,valor,proximo):
        self.inf = valor
        self.prox = proximo
class Pd():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def show(self):
        aux=self.prim
        while aux != None:
            print(aux.inf)
            aux=aux.prox
            
    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1

    def removerFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox != self.ult:
                aux=aux.prox
            self.ult=aux
            aux.prox=None
        self.quant-=1

    def getTopo(self):
        aux=self.prim
        while aux != None:
            print(aux.inf)
            break
        
    def estarVazia(self):
        self.quant==0
