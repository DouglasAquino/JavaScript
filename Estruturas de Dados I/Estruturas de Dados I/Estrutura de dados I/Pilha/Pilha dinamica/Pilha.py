import Pd
class No():
    def __init__(self,valor,proximo):
        self.inf = valor
        self.prox = proximo
class Pilha():
    def __init__(self):
        self.f1=Pd.Pd()
    def inserir(self,valor):
            self.f1.inserirFim(valor)

            
    def show(self):
        self.f1.show()
        
    def remover(self):
        if not self.f1.estarVazia():
               self.f1.removerFim()
    def estarVazia(self):
        if self.f1.quant==0:
            return true
        else:
            return false
    
