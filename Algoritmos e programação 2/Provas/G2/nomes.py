def imprimeMenoresNomes(*nomes):
     
     lista = []
     for i in nomes:
          lista.append(len(i))
     menor = 1000
     for i in range(len(lista)):
          if lista[i] < menor:
               menor = lista[i]
     menornomes = []
     for i in range(len(lista)):
          if lista[i] == menor:
               menornomes.append(nomes[i])
     return menornomes

def retornaPares(pares):
     lista_de_Par = []
     for i in pares:
          if i % 2 == 0:
               lista_de_Par.append(i)
     return lista_de_Par
     
