class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo
class Ldse():
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0
    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1
    def show(self):
        aux=self.prim
        while aux != None:
            print(aux.info)
            aux=aux.prox
    def removerInicio(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1
    def getPrim(self):
        return self.prim.info
    def getUlt(self):
        return self.ult.info
    def getQuant(self):
        return self.quant
    def estahVazia(self):
        return self.quant==0
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
    
    def inserirAposDet(self,valor1,valor2):
        pos=aux=self.prim
        qi=0
        if self.prim.info==valor2:
            self.prim.prox=No(valor1,aux.prox)
            aux=aux.prox
            qi+=1
            self.quant+=1
        while aux != None:
            if aux.info == valor2:
                pos=aux
                pos.prox=No(valor1,aux.prox)
                qi+=1
                self.quant+=1
                if valor2 == self.ult:
                    self.ult.prox=self.ult=No(valor,None)
                    qi+=1
            aux=aux.prox
        return qi
    
    def inserirAntDet(self,valor1,valor2):
        ant=aux=self.prim
        if self.prim.info==valor2:
            self.prim=No(valor1,self.prim)
            aux=aux.prox
            self.quant+=1
        while aux != None:
            if aux.info == valor2:
                ant.prox=No(valor1,aux)
                self.quant+=1
            ant=aux
            aux=aux.prox
            
    def removerDet(self,dado):  #Estuda mais esse intem
        aux = self.prim
        ant = None
        while aux.info!=dado:
            ant = aux
            aux = aux.prox
        if aux == self.prim:
            self.prim = self.prim.prox
            self.quant -= 1
        else:
            ant.prox = aux.prox
            if aux == self.ult:
                self.ult = ant
            self.quant -=1

    def removerAntesD(self,dado):
        aux =self.prim
        ant1 = None
        ant2 = None
        while aux.info!=dado:
            ant2 = ant1
            ant1 = aux
            aux = aux.prox
        if aux.info == dado:
            if ant1 == self.prim:
                self.prim=self.prim.prox
                self.quant -= 1
            else:
               if ant2 != None:
                   ant2.prox = aux
                   self.quant -=1
               else:
                   print('Nao pode ser removido')
        #colocado por mim.
        if self.quant == 1:
            op = input('So tem um elemmento Deseja Removelo:').lower()
            if op == 'sim':
                self.removerFim()
                print('removido')
