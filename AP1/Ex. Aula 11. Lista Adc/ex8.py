numeros = []
maior = 0
qtNegativos = 0
qtMaior = 0
for i in range(10):
    numeros.append(int(input('Numero: ')))
    if maior < numeros[i]:
        maior = numeros[i]
    if numeros[i] < 0:
        qtNegativos = qtNegativos + 1
for i in range(len(numeros)):
    if numeros[i] == maior:
        qtMaior = qtMaior + 1
print(numeros)
print('Maior numero digitado: ', maior)
print('Quantidade de numeros negativos: ', qtNegativos)
print('Quantidade de vezes que o maior se repete: ', qtMaior)
