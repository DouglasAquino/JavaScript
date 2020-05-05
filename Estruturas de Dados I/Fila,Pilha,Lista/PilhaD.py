class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo
class PilhaD():
    def __init__(self):
        self.prim=None
        self.quant=0
        
    def push(self,valor):
        if self.quant==0:
            self.prim=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1

    def pop(self):
        if self.quant==1:
            self.prim=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
    def estahVazia(self):
        return self.quant==0
    
    def getTopo(self):
        return self.prim.info
    def show(self):
        aux=self.prim
        while aux != None:
            print(aux.info)
            aux=aux.prox
