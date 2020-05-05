class les():
    def __init__(self):
        self.lista=[None,None,None,None,None]
        self.quant=0
    def inserirInicio(self,valor):             #inserir valor no inicio da lista empurrando os demais valores para trás.
        for i in range(self.quant,0,-1):
            self.lista[i]=self.lista[i-1]    
        self.lista[0]=valor
        self.quant+=1
    def removerInicio(self):                   #remove o primeiro valor da lista, trazendo as demais uma posição para frente.
        for i in range (self.quant-1):
            self.lista[i]=self.lista[i+1]
        self.quant-=1
    def inserirFim (self, valor):              #inserir valor após o ultimo elemento da lista
            self.lista[self.quant]=valor
            self.quant+=1

    def removerFim (self):                      #remove o ultimo elemento da lista 
        self.lista[self.quant-1]=None
        self.quant-=1
    def inserirAposDet(self,valor1,valor2):      #insere valor1 apos cada ocorrencia de valor 2 enquanto for possivel
        pass
    def inserirAposDetConta(self,valor1,valor2): #insere valor1 após ocorrencia de valor2 
        pass                                     #se possivel retornando a qt de inserçoes 
    def estaCheia(self):
        return self.quant == 5
    def estaVazia(self):
        return self.quant == 0
    def getPrim(self):
        return self.lista[0]
    def getUlti(self):
        return self.lista[self.quant-1]

    def show(self):
        print(self.lista)
