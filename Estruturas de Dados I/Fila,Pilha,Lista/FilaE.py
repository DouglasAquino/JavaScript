class FilaE():
    def __init__(self):
        self.vet=[None,None,None,None,None]
        self.quant=0
    def inserir (self,valor):
        self.vet[self.quant]=valor
        self.quant+=1
        
    def remover (self):
        if self.quant == 1:
            self.vet[self.quant-1] = None
        else:
            i=0
            while i < self.quant-1:
                self.vet[i]=self.vet[i+1]
                i+=1
        self.quant-=1
        
    def getPrim(self):
        return self.vet[0]
    
    def estahVazia(self):
        return self.quant == 0
    
    def estahCheia(self):
        return self.quant == 5
    def show(self):
        for i in range(self.quant):
            print(self.vet[i])
