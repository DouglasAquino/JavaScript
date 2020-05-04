lista = []

preencher = input('Deseja preencher a lista[s/n]?')
while preencher != 'n':
    for i in range(4):
        novalinha = []
        novalinha.append(int(input('Primeiro Número: ')))
        novalinha.append(int(input('Segundo Número: ')))
        novalinha.append(novalinha[0] + novalinha[1])
        if novalinha[2] % 2 == 0:
            novalinha.append(novalinha[2] / 2)
        else:
            novalinha.append(novalinha[2] * 2)
        lista.append(novalinha)
    preencher = input('Deseja continuar?[s/n]?')

for i in range(len(lista)):
    print(lista[i])
print('FIM')
