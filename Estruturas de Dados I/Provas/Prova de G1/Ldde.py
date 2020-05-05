class No():
    def __init__ (self,ant,valor,prox):
        self.ant=ant
        self.info=valor
        self.prox=prox
class Ldde():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None, valor, None)
        else:
            self.prim.ant=self.prim=No(None, valor, self.prim)
        self.quant+=1
    def removerInicio(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
            self.prim.ant=None
        self.quant-=1   
    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None,valor,None)
        else:
            self.ult.prox=self.ult=No(self.ult,valor,None)
        self.quant+=1
    def removerFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.ult=self.ult.ant
            self.ult.prox=None
        self.quant-=1
    def show(self):
        aux=self.prim
        while aux != None:
            print(aux.info)
            aux=aux.prox
    def showReverso(self):
        aux=self.ult
        while aux != None:
            print(aux.info)
            aux=aux.ant
    def getPrim(self):
        return self.prim.info
    def getUlt(self):
        return self.ult.info
    def getQuant(self):
        return self.quant
    def estahVazia(self):
        return self.quant==0

    def inserirAposDet(self,valor1,valor2):
        pos=aux=self.prim
        qi=0
        if self.prim.info == valor2:
            self.prim.prox=No(self.prim,valor1,aux.prox)
            aux=aux.prox
            qi+=1
            self.quant+=1
        while aux!= None:
            if aux.info == valor2:
                if valor2 != self.ult:
                    pos=aux
                    pos.prox=No(aux.ant,valor1,aux.prox)
                    qi+=1
                    self.quant+=1
                else:
                    self.ult.prox=self.ult=No(self.ult.ant,valor1,None)
                    qi+=1
            aux=aux.prox
        return qi

    def existeNaLista(self,valor):
        aux=self.prim
        q=-1
        while aux != None:
            if aux.info == valor:
                q+=1  # se for o primeiro vai retornar zero... 
                return q
        if q == '-1':
            return 0
                
                
