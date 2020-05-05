class Les():
    def __init__(self):
        self.vet=[None,None,None,None,None]
        self.quant=0

    def estahVazia(self):
        return self.quant == 0

    def estahCheia(self):
        return self.quant==5

    def inserirFim(self,valor):
        self.vet[self.quant]=valor
        self.quant+=1

    def show(self):
        for i in range(self.quant):
            print(self.vet[i])

    def removerFim(self):
        self.quant-=1

    def getPrim(self):
        #retorna o primeiro elemento da lista
        return self.vet[0]
    def getUlt(self):
        #retornar o ultimo elemento da lista
        return self.vet[-1]
    def getQuant(self):
        #retornar a quantidade de elemento da lista
        return self.quant
    def inserirInicio(self,valor):
        i=self.quant
        while i > 0:
            self.vet[i]=self.vet[i-1]
            i-=1
        self.vet[0]=valor
        self.quant+=1 
    def removerInicio(self):
        i=0
        while i < self.quant-1:
            self.vet[i]=self.vet[i+1]
            i+=1
        self.quant-=1

    def inserirAposDet(self,valor1,valor2):
        i=0
        qi=0
        while i < self.quant:
            if self.vet[i]== valor2:
                qi+=1
                j=self.quant
                while j > i+1:
                    self.vet[j]=self.vet[j-1]
                    j-=1
                self.vet[j]=valor1
                self.quant+=1
            i+=1
        return qi

    def inseriDepois(self,dado1,dado2):
        pos = 0
        for i in range(self._quant):
            if self._lista[i] == dado2:
                pos = i

        for i in range(self._quant,pos,-1):
            self._lista[i] = self._lista[i+1]
        self._lista[pos] = dado1
        self._quant += 1
