lista = []
i = 0
while i < 10:
    lista.append(input('Nome: '))
    i = i + 1
print(lista)
nome = input('Nome para pesquisar: ')
i = 0
while nome in lista:
    lista.remove(nome)
    i = i + 1
print(lista)
