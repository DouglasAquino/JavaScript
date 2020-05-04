i = 0
lista = []
while i < 10:
    lista.append(int(input('Numero: ')))
    i = i + 1
lista[0] = 0
print(lista)
posicao = []
soma = 0
maior = 0
i = 0
while i < 10:
    if lista[i] < 0:
        posicao.append(i)
    if i < 4:
        soma = soma + lista[i]
    if lista[i] > maior:
        maior = lista[i]
    i = i + 1
lista[0] = maior
print('Posição dos elementos negativos: ', posicao)
print('Soma dos cinco ultimos elementos: ', soma)
print(lista)
