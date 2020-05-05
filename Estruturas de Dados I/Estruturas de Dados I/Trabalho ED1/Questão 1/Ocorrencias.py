class Ocorrencias:
    def __init__ (self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def retorna(self,valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.retorna(valor)

class No:

    def __init__(self,valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self,valor):
        if valor >= self.info:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)
        else:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)

    def retorna(self,valor):
        
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.retorna(valor)
                if aux == 0:
                    return 0
                else:
                    return aux +1
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.retorna(valor)
                if aux == 0:
                    return 0
                else:
                    return aux +1
