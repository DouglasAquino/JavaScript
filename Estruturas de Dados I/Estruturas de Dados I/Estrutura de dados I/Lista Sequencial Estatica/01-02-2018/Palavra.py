class Palavra():
   
    def __init__(self):
        self.letras = [None,None,None,None,None]
        self.quant=0

    def insereLetra(self,letra):
        self.letras[self.quant]=letra
        self.quant+=1

    def imprimePalavra(self):
        i=0
        while i<self.quant:
            print(self.letras[i],end='')
            i+=1
            
    def removeLetra(self):
        #remove a ultima letra da palavra
        self.quant-=1

    def insereLetraInicio(self,letra):
        #insere letra no inicio
        #da palavra(para isso 'imprimir'
        #as demais para trás)
        
        for i in range(self.quant,0,-1):
            self.letras[i]=self.letras[i-1]
        self.letras[0]=letra
        self.quant+=1
  
    def removeLetraInicio(self):
        #remove a primeira letra
        #da palavra trazendo as
        #demais letras para frente
        for i in range(self.quant):
            self.letras[i]=self.letras[i+1]
        self.quant-=1
        
    def palavraCheia(self):
        if self.quant==5:
            return True
        else:
            return False
'''
#Verifica se está cheia ou Vazia('palavra ou lista')...
    def palavraVazia(self):
        return self.quant==0

#Verifica a primeira letra
    def getPrim(self):
        return self.letras[0]
#Verifica a ultima letra
    def getUlt(self):
        return self.letras[self.quant-1]
'''    
