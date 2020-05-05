class Tree:
    def __init__(self):
        self.raiz = None
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()
    def alturaNO(self, valor):
        if self.raiz != None:
            return self.raiz.alturaNO(valor)
    def nivel(self, valor):
         if self.raiz != None:
            return self.raiz.nivel(valor)
    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()
    def maisEsq(self):
        if self.raiz != None:
            return self.raiz.maisEsq()
    def preOrdem(self):
        if self.raiz!=None:
            self.raiz.preOrdem()
class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
    def insere(self, valor):
        if valor <= self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)
    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem()
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
    def somaFolhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq==None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()
    def max(self, a, b):
        if a>b:
            return a
        return b
    def altura(self):
        hesq=hdir=0
        if self.esq!=None:
            hesq=self.esq.altura()
        if self.dir!=None:
            hdir=self.dir.altura()
        return 1 + max(hesq,hdir)
    def nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.nivel(valor)
                if aux != False:
                    return 1 + aux
                else:
                    return False

        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.nivel(valor)
                if aux != False:
                    return 1 + aux
                else:
                    return False
    def maisdir(self):
        if self.dir != None:
            return self.dir.maisdir()
        else:
            return self.info
    def maisEsq(self):
        if self.esq != None:
            return self.esq.maisEsq()
        else:
            return self.info
    def alturaNO(self, valor):
        if valor == self.info:
            return self.altura()
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.alturaNO(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.alturaNO(valor)
    def preOrdem(self):
        print(self.info,end=' ')#se o print ficar na parte de baixo fica em pos ordem
        if self.esq!=None:
            self.esq.preOrdem()
        if self.dir!=None:
            self.dir.preOrdem()

a=Tree()
a.insere(8)
a.insere(4)
a.insere(2)
a.insere(3)
a.insere(1)
a.insere(6)
a.insere(5)
a.insere(7)
a.insere(12)
a.insere(10)
a.insere(9)
a.insere(11)
a.insere(14)
a.insere(13)
a.insere(15)

#print(a.maisEsq())
print(a.preOrdem())
print(a.altura())
