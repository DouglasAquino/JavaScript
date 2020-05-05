import FilaD

class FilaP():
    def __init__(self):
        self.f1=FilaD.FilaD()
        self.f2=FilaD.FilaD()
        self.f3=FilaD.FilaD()
        self.f4=FilaD.FilaD()
        
    def inserir(self,valor,prioridade):
        if prioridade==1:
            self.f1.inserir(valor)
        elif prioridade==2:
            self.f2.inserir(valor)
        elif prioridade==3:
            self.f3.inserir(valor)
        else:
            self.f4.inserir(valor)
            
            
    def remover(self):
        if self.f1.estahVazia()==False:
            self.f1.remover()
        elif self.f2.estahVazia()==False:
            self.f2.remover()
        elif self.f3.estahVazia()==False:
            self.f3.remover()
        else:
            self.f4.remover()

    def estahVazia(self):
        return self.f1.estahVazia()==True and self.f2.estahVazia()==True and self.f3.estahVazia()==True and self.f4.estahVazia()==True

    def show1(self):       
        if self.f1.estahVazia()==False:
            self.f1.show()
        else:
            print('Fila vazia!')

    def show2(self):       
        if self.f2.estahVazia()==False:
            self.f2.show()
        else:
            print('Fila vazia!')

    def show3(self):       
        if self.f3.estahVazia()==False:
            self.f3.show()
        else:
            print('Fila vazia!')

    def show4(self):       
        if self.f4.estahVazia()==False:
            self.f4.show()
        else:
            print('Fila vazia!')
             

        
            

        
        

        
