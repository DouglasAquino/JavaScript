class Les():
    def __init__(self):
        self.lista=[None,None,None,None,None]
        self.quant=0

    def estahVazia(self):
        return self.quant==0
    
    def estahCheia(self):
        return self.quant==5
        
    def push(self,valor):
        self.lista[self.quant]=valor
        self.quant+=1

    def pop(self):
        self.quant-=1
        
    def show (self):
        for i in range(self.quant):
            print(self.lista[i])
            
    def getTopo(self):
        return self.lista[self.quant-1]
