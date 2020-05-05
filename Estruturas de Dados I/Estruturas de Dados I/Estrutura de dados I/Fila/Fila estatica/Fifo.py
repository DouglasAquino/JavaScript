class Fifo():
    def __init__(self):
        self.lista = [None,None,None,None,None]
        self.quant = 0
        
    def inserir(self,valor):
        self.lista[self.quant] = valor
        self.quant+=1

    def remover(self):
        for i in range(self.quant-1):
            self.lista[i] = self.lista[i+1]
        self.quant-=1

    def estarVazia(self):
        return self.quant==0

    def estarCheia(self):
        return self.quant==5

    def getPrim(self):
        return self.lista[0]

    def getUlt(self):
        return self.lista[self.quant-1]

    def show(self):
        for i in range(self.quant):
            print(self.lista[i],end='')
        print()
