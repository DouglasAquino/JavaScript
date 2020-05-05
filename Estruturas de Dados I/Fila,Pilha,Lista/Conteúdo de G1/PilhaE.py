class PilhaE():
    def __init__(self):
        self.vet=[None,None,None,None,None]
        self.quant=0
    def push (self,valor):
        self.vet[self.quant]=valor
        self.quant+=1
        
    def pop (self):
        self.quant-=1
        
    def getTopo(self):
        return self.vet[self.quant-1]
    
    def estahVazia(self):
        return self.quant == 0
    
    def estahCheia(self):
        return self.quant==5

        
