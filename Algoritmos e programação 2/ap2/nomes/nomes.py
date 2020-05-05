def maioresNomes(*nomes):
     '''
     lista = []
     for i in nomes:
          lista.append(len(i))
     maior = 0
     for i in range(len(lista)):
          if lista[i] > maior:
               maior = lista[i]
     maiornomes = []
     for i in range(len(lista)):
          if lista[i] == maior:
               maiornomes.append(nomes[i])
     '''
     l = nomes
     n = list(l)
     max_list = sorted(n, key=len)[-1]
     lmaior = len(max_list)
     lista = []
     for i in nomes:
          if len(i) == lmaior:
               lista.append(i)
     return lista

def imprimePares(pares):
     listaPar = []
     for i in pares:
          if i % 2 == 0:
               listaPar.append(i)
     return listaPar
     
