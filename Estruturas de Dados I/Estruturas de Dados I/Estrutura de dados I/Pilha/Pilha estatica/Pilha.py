import Pd
class Pilha():
    def __init__(self):
        self.f1=Pd.Pd()
        self.f2=Pd.Pd()
    def inserir(self,valor,prio):
        if prio==1:
            self.f1.inserirFim(valor)
        elif prio==2:
            self.f2.inserirFim(valor)
            
    def show(self):
        self.f1.show()
        self.f2.show()
        
    def remover(self):
        if not self.f1.estarVazia():
               self.f1.removerFim()
        else:
               self.f2.removerFim()
