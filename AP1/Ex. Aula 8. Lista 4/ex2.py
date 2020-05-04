listaNomes = []
qtNomes = 0
nome = input('Nome: ')
while nome != 'sair':
    listaNomes.append(nome)
    nome = input('Nome: ')
print(listaNomes)
i = 0
while i < len(listaNomes):
    print(listaNomes[i])
    i = i + 1
nomPesq = input('Nome para contar: ')
i = 0
while i < len(listaNomes):
    if listaNomes[i] == nomPesq:
        qtNomes = qtNomes + 1
    i = i + 1
print('O nome {} aparece {} vezes.'.format(nomPesq, qtNomes))
