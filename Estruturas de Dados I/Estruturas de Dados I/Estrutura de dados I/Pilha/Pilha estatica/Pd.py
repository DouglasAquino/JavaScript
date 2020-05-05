class Pd():
    def __init__(self):
        self.lista = [None,None,None,None,None]
        self.quant = 0
        
    def inserirFim(self,valor):
        self.lista[self.quant] = valor
        self.quant+=1

    def removerFim(self):
        self.quant-=1
        

    def estarVazia(self):
        return self.quant==0

    def getUlt(self):
        return self.lista[self.quant-1]

    def show(self):
        for i in range(self.quant):
            print(self.lista[i],end='')
        print()

