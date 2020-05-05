class No():
    def __init__(self,anterior,valor,proximo):
        self.ant=anterior
        self.info=valor
        self.prox=proximo

class Lddec(): #Lista dinâmica uplamente encadeada circular
    def __init__(self):
        self.prim=None
        self.ult=None
        self.quant=0

    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None,valor,None)
            self.prim.ant=self.prim.prox=self.prim
        else:
            self.prim.ant=self.prim=No(self.ult,valor,self.prim)
            self.ult.prox=self.prim
        self.quant+=1

    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(None,valor,None)
            self.prim.ant=self.prim.prox=self.prim
        else:
            self.ult.prox=self.ult=No(self.ult,valor,self.prim)
            self.prim.ant=self.ult
        self.quant+=1

    

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

    def removerDet(self,valor):
        aux=self.prim
        i=1
        while i<=self.quant:           
            if aux.info==valor:
                if self.quant==1:
                    self.prim=self.ult=None                    
                elif aux==self.prim:
                    self.prim=self.prim.prox
                    self.prim.ant=self.ult
                    self.ult.prox=self.prim
                elif aux==self.ult:
                    self.ult=self.ult.ant
                    self.ult.prox=self.prim
                    self.prim.ant=self.ult
                else:
                    aux.prox.ant=aux.ant
                    aux.ant.prox=aux.prox
                i=self.quant
                self.quant-=1
            aux=aux.prox
            i+=1

    def show(self):
        aux=self.prim
        i=0
        
        while i<self.quant:
            print(aux.info)
            aux=aux.prox
            i+=1
    def showReverse(self):
        aux=self.ult
        i=0
        
        while i<self.quant:
            print(aux.info)
            aux=aux.ant
            i+=1
        
        
        

            
        
        
        
        
        
