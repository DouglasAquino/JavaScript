import Fd
class No():
    def __init__(self,valor,proximo):
        self.inf = valor
        self.prox = proximo
class FilaP():
    def __init__(self):
        self.f1=Fd.Fd()
        self.f2=Fd.Fd()
    def inserir(self,valor,prio):
        if prio==1:
            self.f1.inserir(valor)
        elif prio==2:
            self.f2.inserir(valor)
            
    def show(self):
        self.f1.show()
        self.f2.show()
        
    def remover(self):
        if not self.f1.estarVazia():
               self.f1.remover()
        else:
               self.f2.remover()
    
    def estarVazia(self):
        if self.f1.quant==0 and self.f2.quant==0:
            return true
        else:
            return false
    
