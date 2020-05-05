class No():
    def __init__(self,valor,prox):
        self.info=valor
        self.prox=prox
class Fila():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
    def inserir(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1
    def remover(self):
        if self.quant == 1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
    def estahVazia(self):
        if self.quant == 0:
            return True
        else:
            return False
    def pegaPrim(self):
        return self.prim.info
    

