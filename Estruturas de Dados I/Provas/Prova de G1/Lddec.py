class No():
    def __init__ (self,ant,valor,prox):
        self.ant=ant
        self.info=valor
        self.prox=prox
class Lddec():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None,valor,None)
            self.prim.ant=self.prim.prox=self.prim
        else:
            self.prim.ant=self.prim=self.ult.prox=No(self.ult,valor,self.prim)
        self.quant+=1
    def inserirFim(self,valor):
        if self.quant==0:
            self.ult=self.prim=No(None, valor, None)
            self.ult.prox=self.ult.ant=self.ult
        else:
            self.ult.prox=self.ult=self.prim.ant=No(self.ult,valor,self.prim)
        self.quant+=1
    def show(self):
        aux=self.prim 
        for i in range(self.quant):
            print(aux.info)
            aux=aux.prox 
        
    def inserirAntesDet(self, valor1, valor2):
        ant=aux=self.prim
        qi=0
        
        if self.prim.info == valor2: # e se nao for o prim???
            self.prim.ant=self.prim=No(self.ult,valor1,self.prim)
            aux=aux.prox
            qi+=1
            self.quant+=1

        return qi
