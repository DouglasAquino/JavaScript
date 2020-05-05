class No():
    def __init__(self,anterior,valor,proximo):
        self.ant=anterior
        self.info=valor
        self.prox=proximo

class Lddec():
    def __init__(self):
        self.prim=None
        self.quant=0

    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=No(None,valor,None)
            self.prim.ant=self.prim.prox=self.prim
        else:
            self.prim.ant=self.prim=No(self.prim.ant,valor,self.prim)
            self.prim.ant.prox=self.prim
        self.quant+=1
                    

    def inserirAntesDe(self,valor1,valor2):
        aux=self.prim
        i=1
        
        while i<=self.quant:           
            if aux.info==valor2:
                if aux==self.prim:
                    self.prim.ant=self.prim=No(self.prim.ant,valor1,self.prim)
                else:
                    aux.ant.prox=aux.ant=No(aux.ant,valor1,aux)
                i=self.quant
                self.quant+=1
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
        aux=self.prim.ant
        i=0
        
        while i<self.quant:
            print(aux.info)
            aux=aux.ant
            i+=1
        
        
        

            
        
        
        
        
        
