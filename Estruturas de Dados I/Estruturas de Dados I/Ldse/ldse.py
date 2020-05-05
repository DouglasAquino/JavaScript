class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo

class ldse():
    def __init__(self):
        self.prim=None
        self.ult=None
        self.quant=0
        
    def inserirInicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)

        else:
            self.prim=No(valor,self.prim)

        self.quant+=1


    def inserirFim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)

        else:
            self.ult.prox=self.ult=No(valor,None)

        self.quant+=1

    def show(self):
        aux=self.prim
        
        while aux!=None:
            print(aux.info)
            aux=aux.prox
        
    def removerInicio(self):
        if self.quant==1:
            self.prim=self.ult=None

        else:
            self.prim=self.prim.prox

        self.quant-=1
    
    def removerFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox!=self.ult:
                aux=aux.prox
                
            aux.prox=None
            self.ult=aux
        self.quant-=1
    
    def removerDet(self,valor):
        aux=self.prim
        ant=None
        
        while aux.info!=valor:
            ant=aux
            aux=aux.prox

        if aux!=self.prim:
            ant.prox=aux.prox
            if aux.prox==None:
                self.ult=ant
        else:
            self.prim=aux.prox
        self.quant-=1
    

    def removerAntes(self,valor):
        aux=self.prim
        ant1=None
        ant2=None
        
        while aux.info!=valor1:
            ant2=ant1
            ant1=aux
            aux=aux.prox
            
        if aux.info==valor1:
            if ant1==self.prim:
                self.prim=self.prim.prox
                self.quant-=1
                
            elif ant2 != None:
                ant2.prox=aux
                self.quant-=1
                
            else:
                print('O valor não pode ser removido por não ter elemento antes dele!')
    
    def showReverse(self):
        if self.prim!=None:
            self.imprimirReverse(self.prim)

    def imprimirReverse(self,aux):
        if aux!=None:
            self.imprimirReverse(aux.prox)
            print(aux.info)        
        
    def show(self):
        if self.prim!=None:
            self.imprimir(self.prim)

    def imprimir(self,aux):
        if aux!=None:
            print(aux.info)
            self.imprimir(aux.prox)
                         
            
            
            
        
        
        
