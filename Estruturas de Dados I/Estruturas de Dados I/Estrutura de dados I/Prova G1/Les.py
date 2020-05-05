class Les():
    def __init__(self):
        self.lista = [None,None,None,None,None]
        self.quant = 0
        
    def inserir(self,valor):
        self.lista[self.quant] = valor
        self.quant+=1

    def removerFim(self):
        self.quant-=1

    def esvaziarLista(self):
        aux = self.quant
        while aux != 0:
            self.quant-=1
        
    def imprimir(self):
        for i in range(self.quant):
            print(self.lista[i],end='')
        print()
