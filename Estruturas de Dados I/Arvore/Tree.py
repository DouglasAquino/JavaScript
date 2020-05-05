class Tree:
    
    def __init__(self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz==None:
            self.raiz=No(valor)
        else:
            self.raiz.insere(valor)
            #print("?")
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
            
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
            
    def decrescente(self):
        if self.raiz != None:
            self.raiz.decrescente()

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
        
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
        
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()

    def h(self, valor):
        if self.raiz != None:
            return self.raiz.h(valor)
        
    def nivel(self, valor):
         if self.raiz != None:
            return self.raiz.nivel(valor)
        
    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()

    def maisesq(self):
        if self.raiz != None:
            return self.raiz.maisesq()
        
    def prioridade(self,valor):
        if valor < self.info:
            if self.esq==None:
                self.esq=No(valor)
            else:
                self.esq.prioridade(valor)
        else:
            if self.dir==None:
                self.dir=No(valor)
            else:
                self.dir.prioridade(valor)
        

    def SomaEspecifica(self, valor):
        if self.raiz != None:
            return self.raiz.SomaEspecifica(valor)
     
    def somafolhasEspecifica(self, valor):
        if self.raiz != None:
            return self.raiz.somafolhasEspecifica(valor)
        
    def quantidade(self, valor):
        if self.raiz != None:
            return self.raiz.quantidade(valor)

    def MaioresQ(self, valor):
         if self.raiz != None:
            return self.raiz.MaioresQ(valor)

    def MenoresQ(self, valor):
         if self.raiz != None:
            return self.raiz.MenoresQ(valor)
        
    def somaMaiores(self, valor):
        if self.raiz != None:
            return self.raiz.somaMaiores(valor)

    def somaMenores(self, valor):
        if self.raiz != None:
            return self.raiz.somaMenores(valor)

    def printDescendentes(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.printDescendentes(valor)

    def printCaminho(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.printCaminho(valor)
        


    
class No:
    def __init__(self,valor):
        self.info=valor
        self.esq=None #menor q o pai.
        self.dir=None #maior q o pai.
        
    def insere(self,valor):
        if valor<=self.info:
            if self.esq==None:
                self.esq=No(valor)
                #print("*")
            else:
                self.esq.insere(valor)
                #print("+")
        else:
            if self.dir==None:
                self.dir=No(valor)
                #print("-")
            else:
                self.dir.insere(valor)
                #print("#")
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

    def inOrdem (self): #crescente
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end=" ")
        if self.dir != None:
            self.dir.inOrdem()
    def decrescente(self):
        print(self.info,end=" ")
        if self.dir != None:
            self.dir.decrescente()
        if self.esq != None:
            self.esq.decrescente()
                
    def preOrdem(self):
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()

    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end=" ")

    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
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
    def somafolhasEspecifica(self, valor):
        if valor == self.info:
             return self.somaFolhas()
        elif valor <= self.info:
            if self.esq == None:
                return 0
            else:
                return self.esq.somafolhasEspecifica(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.somafolhasEspecifica(valor)
        
    def max(self, a, b):
        if a>b:
            return a
        return b

    def altura(self):
        hesq = hdir=0
        if self.esq != None:
            hesq=self.esq.altura()
            
        if self.dir != None:
            hdir=self.dir.altura()
            
        return 1 + max(hesq, hdir)
        
        
    
    def h(self, valor):
         if valor == self.info:
             return self.altura()
         elif valor < self.info:
            if self.esq == None:
                 return False
            else:
                 return self.esq.h(valor)
         else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)
            
    def nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.nivel(valor)
                if aux != False:
                    return 1+aux
                else:
                    return False
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.nivel(valor)
                if aux != False:
                    return 1+aux
                else:
                    return False

    def maisdir(self):
        if self.dir!=None:
            return self.dir.maisdir()
        else:
            return self.info
        
    def maisesq(self):
        if self.esq!=None:
            return self.esq.maisesq()
        else:
            return self.info

    def prioridade(self,valor):
        if valor < self.info:
            if self.esq==None:
                self.esq=No(valor)
                print("*")
            else:
                self.esq.prioridade(valor)
                print("+")
        else:
            if self.dir==None:
                self.dir=No(valor)
                print("-")
            else:
                self.dir.prioridade(valor)
                print("#")

    def SomaEspecifica(self, valor):
        if valor == self.info:
             return self.soma()
        elif valor <= self.info:
            if self.esq == None:
                 return 0
            else:
                 return self.esq.SomaEspecifica(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.SomaEspecifica(valor)


    def quantidade (self, valor):
        if valor == self.info:
            if self.esq != None:
                return 1 + self.esq.quantidade(valor)
            else:
                return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return self.esq.quantidade(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.quantidade(valor)
      
    def MaioresQ (self, valor):
        if valor == self.info:
            if self.dir != None:
                self.dir.inOrdem()
            return True
        
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.MaioresQ(valor)
                print(self.info)
                if aux == True and self.dir != None:
                    self.dir.inOrdem()
                return True
            
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.MaioresQ(valor)
            
    def MenoresQ (self, valor):
        if valor == self.info:
            if self.esq != None:
                self.esq.inOrdem()
            return True
        
        elif valor >= self.info:
            if self.dir == None:
                return False
            else:
                aux = self.dir.MenoresQ(valor)
                print(self.info)
                if aux == True and self.esq != None:
                    self.esq.inOrdem()
                return True
            
        else:
            if self.esq == None:
                return False
            else:
                return self.esq.MenoresQ(valor)

    def somaMaiores(self, valor):
        if valor == self.info:
            if self.dir != None:  
                return self.dir.soma()
            else:
                return 0
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.somaMaiores(valor)
                if aux and self.dir!=None:
                     return aux + self.dir.soma() + self.info
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.somaMaiores(valor)
            
    def somaMenores(self, valor):
        if valor == self.info:
            if self.esq != None:  
                return self.esq.soma()
            else:
                return 0
        elif valor > self.info:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.somaMenores(valor)
                if aux and self.esq!=None:
                     return aux + self.esq.soma() + self.info
        else:
            if self.esq == None:
                return 0
            else:
                return self.esq.somaMenores(valor)

    def printDescendentes(self, valor):
        if valor == self.info:
            if self.dir != None:
                print (self.dir.inOrdem())
            if self.esq != None:
                print (self.esq.inOrdem())

            else:
                print('Folha')

        elif valor < self.info:
            if self.esq == None:
                 return False
            else:
                 return self.esq.printDescendentes(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.printDescendentes(valor)

    def printCaminho(self, valor):
        if valor == self.info:
             print( self.info)
             
             
        elif valor <= self.info:
            if self.esq == None:
                 return False
            else:
                 aux = self.esq.printCaminho(valor)
                 print( self.info)
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.printCaminho(valor)
                print( self.info)
    
        


