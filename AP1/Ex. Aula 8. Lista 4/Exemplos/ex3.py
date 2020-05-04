lista = [10, 20, 30, 30, 10, 20, 10]
print(lista)
#remover todos os numeros 10 da lista
while 10 in lista:
    lista.remove(10) #remove pelo conteudo
print(lista)
#remover o elemento que esta na primeira posicao
lista.pop(0)
print(lista)
