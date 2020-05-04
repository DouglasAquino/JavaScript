nome = []
i = 0
while i < 10:
    nome.append(input('Nome: '))
    i = i + 1
nomExc = input('Nome para excluir: ')
while nomExc != 'sair':
    i = 0
    while i < len(nomes):
        if nomes[i] == nomExc:
            nomes.pop([i])
        i = i + 1
    print(nomes)
    nomExc = input('Nome para excluir: ')
print(nomes)
