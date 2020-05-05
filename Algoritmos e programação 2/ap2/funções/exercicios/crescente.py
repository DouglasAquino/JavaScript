'''6.	Faça uma função que recebe 3 valores inteiros como argumento e retorna-os ordenados em ordem crescente.
Os valores retornados devem estar separados por vírgula (,) e para serem retornados como uma string,
cada valor deve ser convertido para uma string com o uso da função str(),
que recebe como argumento um número e retorna uma string.'''


def valores(a, b, c):
     lista = [a, b, c]
     lista.sort()
     for i in range(len(lista)):
          lista[i] = str(lista[i])
     return lista

     
