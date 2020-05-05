class Tree:
    
    def __init__(self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz==None:
            self.raiz=No(valor)
        else:
            self.raiz.insere(valor)
    def somaFolhasDescendentes(self, valor):
        if self.raiz != None:
            return self.raiz.somaFolhasDescendentes(valor)
        
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()


    
class No:
    def __init__(self,valor):
        self.info=valor
        self.esq=None
        self.dir=None 
        
    def insere(self,valor):
        if valor<=self.info:
            if self.esq==None:
                self.esq=No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir==None:
                self.dir=No(valor)
            else:
                self.dir.insere(valor)
    def somaFolhasDescendentes(self, valor):
        if valor == self.info:
             return self.somaFolhas() # está somando o proprio valor se for folha... qual seria sua saida pra isso?
        elif valor <= self.info:
            if self.esq == None:
                return 0
            else:
                return self.esq.somaFolhasDescendentes(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.somaFolhasDescendentes(valor)
    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total

        
