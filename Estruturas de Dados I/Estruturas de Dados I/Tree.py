class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
            #print('?', end = '')
            
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
            
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
            
    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()

    def busca(self, valor):
        if self.raiz == None:
            return False
        
        else:
            return self.raiz.busca(valor)

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()

    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
            
    def max(self, valor1, valor2):
        if self.raiz != None:
            return self.raiz.max(valor1, valor2)

    def alturaArvore(self):
        if self.raiz != None:
            return self.raiz.alturaArvore()
        
    def alturaNo(self, valor):
        if self.raiz != None:
            return self.raiz.alturaNo(valor)
        
    def nivelNo(self, valor):
         if self.raiz != None:
            return self.raiz.nivelNo(valor)
        
    def valorMaisDir(self):
        if self.raiz != None:
            return self.raiz.valorMaisDir()
        
    def valorMaisEsq(self):
        if self.raiz != None:
            return self.raiz.valorMaisEsq()
        
    def conta(self):
        if self.raiz != None:
            return self.raiz.conta()

    def contaDescendentes(self,valor):
        if self.raiz != None:
            return self.raiz.contaDescendentes(valor)

    def decresce(self):
        if self.raiz != None:
            self.raiz.decresce()
            
    def retornaMenorQue(self,valor):
        if self.raiz.info == valor:
            return None
        else:
            return self.raiz.retornaMenorQue(valor)
        
    def retornaPai(self,valor):
        if self.raiz.info == valor:
            return None
        else:
            return self.raiz.retornaPai(valor)
        
    def retornaIrmao(self,valor):
        if self.raiz.info == valor:
            return None
        else:
            return self.raiz.retornaIrmao(valor)

    def retornaMenorQue(self,valor):
        if self.raiz != None:
            return self.raiz.retornaMenorQue(valor)

    def balanceamento(self):
        if self.raiz != None:
            return self.raiz.balanceamento()

class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
       
    def insere(self, valor):
         if valor <= self.info:
            #print(valor,'-', self.info)#, 'v < s.i')
            if self.esq == None:
                 self.esq = No(valor)
                 #print('*', end = '')
                 
            else:
                 self.esq.insere(valor)
                 #print('+', end = '')
                 
         else:
             #print(valor,'-', self.info)#, 'v > s.i')
             if self.dir == None:
                 self.dir = No(valor)
                 #print('-', end = '')
                 
             else:
                 self.dir.insere(valor)
                 #print('#', end = '')

    def preOrdem(self):
        print(self.info,end=" ")
        
        if self.esq != None:
            self.esq.inOrdem()
        
        if self.dir != None:
            self.dir.inOrdem()
    
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
            
        print(self.info,end=" ")
        
        if self.dir != None:
            self.dir.inOrdem()

    def posOrdem(self):        
        if self.esq != None:
            self.esq.inOrdem()
        
        if self.dir != None:
            self.dir.inOrdem()
            
        print(self.info,end=" ")
 
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
            #print('\nFolhas: ', end = '')
            print(self.info, end = '')
            
        if self.dir != None:
            self.dir.printFolhas()

    def max(self, valor1, valor2):
        if valor1 > valor2:
            return valor1
        return valor2
    
    def alturaArvore(self):
        hesq = hdir = 0
        
        if self.esq != None:
            hesq = self.esq.alturaArvore()
            
        if self.dir != None:
            hdir = self.dir.alturaArvore()
            
        return 1 + max(hesq, hdir)
    
    def alturaNo(self, valor):
        if valor == self.info:
            return valor
        
        elif valor <= self.info:
            if self.esq == None:
                return False
            
            else:
                return self.esq.alturaNo(valor)
            
        else:
            if self.dir == None:
                return False
            
            else:
                return self.dir.alturaNo(valor)

    def nivelNo(self, valor):
        if valor == self.info:
            return 1
        
        elif valor <= self.info:
            if self.esq == None:
                return False
            
            else:
                aux = self.esq.nivelNo(valor)
                
                if aux != False:
                    return 1 + aux
                
                else:
                    return False
        else:
            if self.dir == None:
                return False
            
            else:
                aux = self.dir.nivelNo(valor)
                
                if aux != False:
                    return 1 + aux
                
                else:
                    return False
                
    def valorMaisDir(self):
        if self.dir != None:
            return self.dir.valorMaisDir()
        
        else:
            return self.info
        
    def valorMaisEsq(self):
        if self.esq != None:
            return self.esq.valorMaisEsq()
        
        else:
            return self.info

    def conta(self):
        filhos = 0
        
        if self.esq != None:
            filhos += self.esq.conta()+1
            
        if self.dir != None:
            filhos += self.dir.conta()+1
            
        return filhos
    
    def contaDescendentes(self,valor):
        filhos = 0
        
        if self.info == valor:
            filhos = self.conta()
            
        elif valor < self.info:
            filhos = self.esq.contaDescendentes(valor)
            
        else:
            filhos = self.dir.contaDescendentes(valor)
            
        return filhos
        
    def decresce(self):
        if self.dir != None:
            self.dir.decresce()
            
        if self.dir != None or self.esq != None:
            print(self.info,end=" ")
            
        if self.esq != None:
            self.esq.decresce()
    
    def retornaPai(self,valor):
        pai = None
        
        if self.dir.info == valor or self.esq.info == valor:
            return self.info
        
        elif valor < self.info:
            pai = self.esq.retornaPai(valor)
            
        else:
            pai = self.dir.retornaPai(valor)

        return pai
        
    def retornaIrmao(self,valor):
        irmao = None
        
        if self.dir.info == valor:
            if self.esq != None:
                return self.esq.info
            
        elif self.esq.info == valor:
            if self.dir != None:
                return self.dir.info
            
        elif valor < self.info:
            irmao = self.esq.retornaIrmao(valor)
            
        else:
            irmao = self.dir.retornaIrmao(valor)
            
        return irmao

    def retornaMenorQue(self,valor):
        menor = None

    def balanceamento(self):
        e = d = 0
        if self.esq != None:
            e = self.esq.alturaArvore()
        if self.dir != None:
            d = self.dir.alturaArvore()
        return d - e 
    


