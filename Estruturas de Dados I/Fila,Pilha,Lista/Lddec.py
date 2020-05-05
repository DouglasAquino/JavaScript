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
    def showReverso(self):
        aux=self.ult
        for i in range(self.quant):
            print(aux.info)
            aux=aux.ant
    def removerInicio(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
            self.prim.ant=self.ult
            self.ult.prox=self.prim
        self.quant-=1
    def removerFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.ult=self.ult.ant
            self.ult.prox=self.prim
            self.prim.ant=self.ult
        self.quant-=1
    def removerDet(self, valor):
        cont = self.quant
        aux = self.prim
        for i in range(self.quant):
            if aux.info == valor:
                self.quant -= 1
                if aux == self.prim:
                    self.prim = aux.prox
                    self.prim.ant = aux.ant
                    aux.ant.prox = self.prim
                else:
                    if aux.prox == self.prim:
                        self.prim.ant = aux.ant
                        aux.ant.prox = aux.prox
                    else:
                        aux.ant.prox = aux.prox
                        aux.prox.ant = aux.ant
            aux = aux.prox
        if self.quant == 0:
            self.prim = None
    def inserirAntesDet(self,dado1,dado2):
        if self.quant == 0:
            print('nao tem antes',dado1)
        else:
            aux = self.prim
            for i in range(self.quant):
                if aux.info == dado1:
                    aux.ant.prox=aux.ant= No(aux.ant,dado2,aux)
                    if aux == self.prim:
                        self.prim = aux.ant
                aux = aux.prox
        self.quant +=1
	
        def inseriAntesDe(self,dado1,dado2): #isso e de todos os que aparecer.
         aux=self.prim
        Qt = 0
        for i in range (self.quant):
            if aux.info == dado2:
                self.quant += 1
                Qt +=1
                aux.ant.prox=aux.ant = No(aux.ant,dado1,aux)
                if aux == self.prim:
                    self.prim = aux.ant
            aux = aux.prox
    def inserirDepoisDet(self,dado1,dado2):
        if self.quant == 0:
            print('nao tem antes',dado1)
        else:
            aux = self.prim
            for i in range(self.quant):
                if aux.info == dado1:
                    aux.prox.ant=aux.prox = No(aux,dado2,aux.prox)
                    if aux == self.prim:
                        self.prim = aux.prox
                aux = aux.prox
        self.quant += 1

