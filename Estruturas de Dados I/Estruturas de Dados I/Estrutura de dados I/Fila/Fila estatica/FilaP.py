import Fifo
class FilaP():
    def __init__(self):
        self.f1=Fifo.Fifo()
        self.f2=Fifo.Fifo()
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
