lista = []
nome = input('Nome: ')
while nome != 'sair':
    lista.append(nome)
    nome = input('Nome: ')
print(lista)
for i in range(len(lista)):
    print('Nome: ', lista[i], 'Posição: ', i)
