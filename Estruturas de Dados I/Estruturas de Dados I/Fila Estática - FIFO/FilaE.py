class FilaE():
    def __init__(self):
        self.lista=[None,None,None,None,None]
        self.quant=0

    def estahVazia(self):
        return self.quant==0
    
    def estahCheia(self):
        return self.quant==5

    def inserir(self,valor):
        self.lista[self.quant]=valor
        self.quant+=1

    def remover(self):
        i=0
        while i<self.quant-1:
            self.lista[i]=self.lista[i+1]
            i+=1
        self.quant-=1
        
    def inserir(self,valor):
        self.lista[self.quant]=valor
        self.quant+=1
        
    def show (self):
        for i in range(self.quant):
            print(self.lista[i])

    def getPrim(self):
        return self.lista[0]

 

    
                
                 
                       
                    
        
        
        
