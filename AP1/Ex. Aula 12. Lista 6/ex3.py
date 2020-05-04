lista = []
soma = []
for i in range(50):
    nova = []
    nova.append(input('Nome: '))
    nova.append(input('Setor: '))
    nova.append(float(input('Nota da prova Escrita: ')))
    nova.append(float(input('Nota da prova Pratica: ')))
    lista.append(nova)
for i in range(len(lista)):
    print('\nNome: ', lista[i][0], '\nSetor: ', lista[i][1], '\nNota da prova Escrita: ', lista[i][2], '\nNota da prova Pratica: ', lista[i][3])
    soma.append(lista[i][2] + lista[i][3])
for i in range(len(lista)):
    if soma[i] >= 7:
        print('Nome de quem tirou nota 7 ou maior: ', lista[i][0])
setorpesq = input('Setor para pesquisa: ')
for i in range(len(lista)):
    if setorpesq == lista[i][1]:
        print('Funcionario do setor: ', setorpesq, 'Sao: ', lista[i][0])
