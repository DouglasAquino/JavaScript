import FilaE
class FilaPri():
    def __init__(self):
        self.F1=FilaE.FilaE()
        self.F2=FilaE.FilaE()
        self.F3=FilaE.FilaE()
        self.F4=FilaE.FilaE()
        
    def inserir(self,nome, pri):
        if pri == 1:
            self.F1.inserir(nome)
            
        elif pri == 2:
            self.F2.inserir(nome)
            
        elif pri == 3:
            self.F3.inserir(nome)

        elif pri == 4:
            self.F4.inserir(nome)
            
    def remover(self):
        if not self.F1.estahVazia():
            self.F1.remover()

        elif not self.F2.estahVazia():
            self.F2.remover()

        elif not self.F3.estahVazia():
            self.F3.remover()

        elif not self.F4.estahVazia():
            self.F4.remover()
 
    def estahVazia(self):
        return self.F1.estahVazia() and self.F2.estahVazia() and self.F3.estahVazia() and  self.F4.estahVazia()
     
    def getPrim(self):
        if not self.F1.estahVazia():
            return self.F1.getPrim()

        elif not self.F2.estahVazia():
            return self.F2.getPrim()

        elif not self.F3.estahVazia():
            return self.F3.getPrim()

        elif not self.F4.estahVazia():
            return self.F4.getPrim()

    def show(self): #Apenas para vizualizar o que esta acontecendo
        self.F1.show()
        self.F2.show()
        self.F3.show()
        self.F4.show()
