import random
numeros = []
i = 0
while i < 50:
    numeros.append(random.randint(-50, 50))
    i = i + 1
print('Numeros: ', numeros)
soma = 0
qt20e50 = 0
novaLista = []
i = 0
while i < 50:
    if i >= 40:
        soma = soma + numeros[i]
    if numeros[i] >= 20 and numeros[i] <=50:
        qt20e50 = qt20e50 + 1
    if numeros[i] % 2 == 0 and numeros[i] < 0:
        novaLista.append(numeros[i])
    i = i + 1
print('A soma: ', soma)
print('A quantidade de números entre 20 e 50 que foram inseridos na lista: ', qt20e50)
print('Pares negativos: ', novaLista)

