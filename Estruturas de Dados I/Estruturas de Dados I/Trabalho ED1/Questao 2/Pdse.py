class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo

class Pdse():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0


    def insereInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            selfprim=No(valor,self.prim)
        self.quant+=1

    def removerInicio(self):
        if self.quant == 1:
            sel.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant-=1

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux=aux.prox

    def estaVazia(self):
        return self.quant == 0

    def getPrim(self):
        return self.prim.info
