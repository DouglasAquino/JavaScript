class Nopai:
    def __init__(self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def paiDe(self,valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.paiDe(valor)


class No:

    def __init__(self,valor):
        self.info=valor
        self.esq=None
        self.dir=None

    def insere(self,valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def paiDe(self,valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            elif self.esq.info == valor:
                return self.info
            else:
                aux = self.esq.paiDe(valor)
                if aux == 0:
                    return 0
                elif self.esq.info == valor:
                    return self.info
                else:
                    return aux
        else:
            if self.dir == None:
                return 0
            elif self.dir.info == valor:
                return self.info
            else:
                aux = self.dir.paiDe(valor)
                if aux == 0:
                    return 0
                elif self.esq.info == valor:
                    return self.info
                else:
                    return aux
