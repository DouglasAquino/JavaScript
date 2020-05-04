lista = [8, 7, 20, 5, 4, 6, 3, 7, 2, 8, 9, 20, 15, 8, 7]
somaPares = 0
pri = 0
maior = 0
qtMaior = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        somaPares = somaPares + lista[i]
    if lista[i] == lista[0]:
        pri = pri + 1
    if lista[i] > maior:
        maior = lista[i]
for i in range(len(lista)):
    if lista[i] == maior:
        qtMaior = qtMaior + 1
print('Soma dos pares: ', somaPares)
print('Quantidade de vezes que o primeiro se repete: ', pri)
print('O maior elemento: ', maior)
print('Quantas vezes o maior se repete: ', qtMaior)
            
