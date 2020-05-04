lista = []
soma = []
maior = 0
for i in range(10):
    nota = []
    nota.append(int(input('Nota do primeiro jurado: ')))
    nota.append(int(input('Nota do segundo jurado: ')))
    nota.append(int(input('Nota do terceiro jurado: ')))
    lista.append(nota)
    soma.append(lista[i][0] + lista[i][1] + lista[i][2])
for i in range(len(lista)):
    print('\nParticipante: ', i, '\nNota do primeiro jurado: ', lista[i][0], '\nNota do segundo jurado: ', lista[i][1], '\nNota do terceiro jurado: ', lista[i][2], '\nSoma total das notas: ', soma[i])
    if maior < soma[i]:
        maior = soma[i]
for i in range(len(lista)):
    if soma[i] == maior:
        print('Codigo: ', i)
