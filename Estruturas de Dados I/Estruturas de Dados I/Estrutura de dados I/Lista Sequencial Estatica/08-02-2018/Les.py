#(les) Lista Estatica Sequencial
class Les():
    def __init__(self):
        self.lista = [None,None,None,None,None]
        self.quant = 0
        
#insere valor no início da palavra para isso 'empurra' demais valores para tras
    def inserirInicio(self,valor):
        for i in range(self.quant,0,-1):
            self.lista[i] = self.lista[i-1]
        self.lista[0] = valor
        self.quant+=1

#insere valor após ultimo elemento da lista
    def inserirFim(self,valor):
        self.lista[self.quant] = valor
        self.quant+=1

#remove o último elemento da lista
    def removerFim(self):
        self.quant-=1
        

#remove a primeiro elemento da lista
    def removerInicio(self):
        for i in range(self.quant-1):
            self.lista[i] = self.lista[i+1]
        self.quant-=1

#retorna True se lista vazia e False caso contrário
    def estarVazia(self):
        return self.quant==0

#retorna True se lista cheia e False caso contrário
    def estarCheia(self):
        return self.quant==5

#retorna o primeiro elemento da lista (retorna nada se lista vazia)
    def getPrim(self):
        return self.lista[0]

#retorna o último elemento da lista (retorna nada se lista vazia)
    def getUlt(self):
        return self.lista[self.quant-1]

#imprime todos os elementos da lista
    def show(self):
        for i in range(self.quant):
            print(self.lista[i],end='')
        print()

#insere valor1 após cada ocorrência de valor2 enquanto for possível
    def inserirAposDet(self,valor1,valor2):
        for x in range(5):
            if self.lista[x] == valor2:
                for i in range(4,x,-1):
                    self.lista[i] = self.lista[i-1] 
                if self.quant <5:
                    self.lista[x+1] = valor1
                    self.quant += 1

#insere valor1 após cada ocorrência de valor2 enquanto for possível retornando
#a quantidade de inserções realizadas
    def inserirAposDetConta(self,valor1,valor2):
        cont = 0
        for x in range(self.quant):
            if self.lista[x] == valor2:
                for i in range(4,x,-1):
                    self.lista[i] = self.lista[i-1] 
                if self.quant <5:
                    self.lista[x+1] = valor1
                    self.quant += 1
                    cont+=1
        return cont
#Fazer também um programa "inteligente" de teste
