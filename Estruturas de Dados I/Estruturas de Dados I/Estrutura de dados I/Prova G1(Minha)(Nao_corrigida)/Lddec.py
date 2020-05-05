class No():
    def __init__(self,anterior,valor,proximo):
        self.ant=anterior
        self.info=valor
        self.prox=proximo

class Lddec():
    def __init__(self):
        self.prim=None
        self.quant=0

    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=No(None,valor,None)
        else:
            self.prim.prox=No(self.prim,valor,None)
        self.quant+=1

    def imprimir(self):
        aux=self.prim
        i=0
        while i<self.quant:
            print(aux.info)
            aux=aux.prox
            i+=1

