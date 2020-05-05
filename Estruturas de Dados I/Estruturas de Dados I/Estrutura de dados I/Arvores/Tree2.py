class No:
    def __init__(self,valor):
        self.info=valor
        self.esq=None
        self.dir=None

    def insere(self,valor):
        if valor< self.info:
            if self.esq==None:
                self.esq=No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir==None:
                self.dir=No(valor)
            else:
                self.dir.insere(valor)

    def busca(self,valor):
        if self.info==valor:
            return True
        elif valor<self.info:
            if self.esq==None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir==None:
                return False
            else:
                return self.dir.busca(valor)

    def printCaminho(self,valor):
        if self.info==valor:
            print(self.info,end='')
            return True
        elif valor<self.info:
            if self.esq==None:
                return False
            else:
                aux=self.esq.printCaminho(valor)
                if aux!=None:
                    print(self.info,end='')
                    return True
                else:
                    return False
        else:
            if self.dir==None:
                return False
            else:
                aux=self.dir.printCaminho(valor)
                if aux!=False:
                    print(self.info,end='')
                    return True
                else:
                    return False

    def preOrdem(self):
        print(self.info,end='')
        if self.esq!=None:
            self.esq.preOrdem()
        if self.dir!=None:
            self.dir.preOrdem()

    def inOrdem(self):
        if self.esq!=None:
            self.esq.inOrdem()
        print(self.info,end='')
        if self.dir!=None:
            self.dir.inOrdem()

    def posOrdem(self):
        if self.esq!=None:
            self.esq.posOrdem()
        if self.dir!=None:
            self.dir.posOrdem()
        print(self.info,end='')

    def printFolhas(self):
        if self.esq!=None:
            self.esq.printFolhas()
        if self.esq==None and self.dir==None:
            print(self.info,end='')
        if self.dir!=None:
            self.dir.printFolhas()

    def printFolhasRevers(self):
        if self.dir!=None:
            self.dir.printFolhas()
        if self.esq==None and self.dir==None:
            print(self.info,end='')
        if self.esq!=None:
            self.esq.printFolhas()

    def soma(self):
        total=self.info
        if self.esq!=None:
            total+=self.esq.soma()
        if self.dir!=None:
            total+=self.dir.soma()
        return total

    def somaFolhas(self):
        total=0
        if self.esq==None and self.dir==None:
            total=self.info
        if self.esq!=None:
            total+=self.esq.somaFolhas()
        if self.dir!=None:
            total+=self.dir.somaFolhas()
        return total

    def contaNosAteFolha(self,valor):
        if self.info==valor:
            return self.altura()
        elif valor<self.info:
            if self.esq==None:
                return False
            else:
                return self.esq.contaNosAteFolha(valor)
        else:
            if self.dir==None:
                return False
            else:
                return self.dir.contaNosAteFolha(valor)

    def nivel(self,valor):
        if self.info==valor:
            return 1
        elif valor<self.info:
            if self.esq==None:
                return False
            else:
                aux=self.esq.nivel(valor)
                if aux!=False:
                    return aux+1
                else:
                    return False
        else:
            if self.dir==None:
                return False
            else:
                aux=self.dir.nivel(valor)
                if aux!=False:
                    return aux+1
                else:
                    return False

    def altura(self):
        alturaEsq=1
        alturaDir=1
        if self.esq!=None:
            alturaEsq+=self.esq.altura()
        if self.dir!=None:
            alturaDir+=self.dir.altura()
        return max(alturaDir,alturaEsq)

    def alturaNo(self,valor):
        if self.info==valor:
            return self.altura()
        elif valor<self.info:
            if self.esq==None:
                return False
            else:
                return self.esq.alturaNo(valor)
        else:
            if self.dir==None:
                return False
            else:
                return self.dir.alturaNo(valor)

    def maiorValor(self):
        if self.dir!=None:
            return self.dir.maiorValor()
        else:
            return self.info

    def menorValor(self):
        if self.esq!=None:
            return self.esq.menorValor()
        else:
            return self.info

class Tree:
    def __init__(self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz==None:
            self.raiz=No(valor)
        else:
            self.raiz.insere(valor)

    def busca(self,valor):
        if self.raiz==None:
            return False
        else:
            return self.raiz.busca(valor)

    def preOrdem(self):
        if self.raiz!=None:
            self.raiz.preOrdem()

    def inOrdem(self):
        if self.raiz!=None:
            self.raiz.inOrdem()

    def posOrdem(self):
        if self.raiz!=None:
            self.raiz.posOrdem()

    def printFolhas(self):
        if self.raiz!=None:
            self.raiz.printFolhas()

    def printFolhasReverse(self):
        if self.raiz!=None:
            self.raiz.printFolhasReverse()

    def soma(self):
        if self.raiz!=None:
            self.raiz.soma()

    def somaFolhas(self):
        if self.raiz!=None:
            self.raiz.somaFolhas()

    def nivel(self,valor):
        if self.raiz!=None:
            self.raiz.nivelNo(valor)

    def altura(self):
        if self.raiz!=None:
            self.raiz.altura()

    def alturaNo(self,valor):
        if self.raiz!=None:
            self.raiz.alturaNo(valor)

    def maiorValor(self):
        if self.raiz!=None:
            self.raiz.maiorValor()

    def menorValor(self):
        if self.raiz!=None:
            self.raiz.menorValor()

