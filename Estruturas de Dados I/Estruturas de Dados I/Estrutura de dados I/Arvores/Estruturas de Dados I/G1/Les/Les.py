class Les():
    def __init__(self):
        self.lista=[None,None,None,None,None]
        self.quant=0

    def estahVazia(self):
        return self.quant==0
    
    def estahCheia(self):
        return self.quant==5

    def esvaziarLista(self):
        for i in range(self.quant):
            self.lista[i]=None
        self.quant=0

    def inserirInicio(self,valor):
        i=self.quant
        while i>0:
            self.lista[i]=self.lista[i-1]
            i-=1
        self.lista[0]=valor
        self.quant+=1

    def removerInicio(self):
        i=0
        while i<self.quant-1:
            self.lista[i]=self.lista[i+1]
            i+=1
        self.quant-=1
        
    def inserirFim(self,valor):
        self.lista[self.quant]=valor
        self.quant+=1

    def removerFim(self):
        self.quant-=1
        
    def show (self):
        for i in range(self.quant):
            print(self.lista[i])

    def getPrim(self):
        return self.lista[0]

    def getUlt(self):
        return self.lista[self.quant-1]


    def inserirAntes(self,valor1,valor2):
        pos=0
        for i in range(self.quant):
            if self.lista[i]==valor2:
                pos=i
        for i in range(self.quant,pos,-1):
            self.lista[i]=self.lista[i-1]
        self.lista[pos]=valor1
        self.quant+=1

    def inserirApos(self,valor1,valor2):
        pos=0
        for i in range(self.quant):
            if self.lista[i]==valor2:
                pos=i
        for i in range(self.quant,pos+1,-1):
            self.lista[i]=self.lista[i-1]
        self.lista[pos+1]=valor1
        self.quant+=1

    def removerDet(self,valor):
        pos=0
        for i in range(self.quant):
            if self.lista[i]==valor:
                pos=i
        self.lista[pos]=None
     
        for i in range(pos,self.quant-1):
            self.lista[i]=self.lista[i+1]
        self.quant-=1

    def localizaPos(self,valor):
        pos=0
        for i in range(self.quant):
            if self.lista[i]==valor:
                pos=i
        return pos

    
                
                 
                       
                    
        
        
        
