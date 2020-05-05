class Tree:
    def __init__(self):
        self.raiz = None
    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    def printCaminho(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.printCaminho(valor) # nao precisava do return



class No:
    def __init__(self,valor):
        self.info = valor
        self.esq = None
        self.dir = None
    def insere(self,valor):
        if valor<=self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)
    
    def printCaminho(self, valor):
        if valor == self.info:
            print(self.info, end=" ")
        elif valor < self.info:
            print(self.info, end = " ")
            self.esq.printCaminho(valor)
        else:
            print(self.info, end = " ")
            self.dir.printCaminho(valor)
