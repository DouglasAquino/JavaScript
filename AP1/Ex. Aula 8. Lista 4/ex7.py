lista = []
i = 0
soma = 0
maior5 = 0
while i < 10:
    lista.append(int(input('Numero: ')))
    i = i + 1
print(lista)
i = 0
while i < len(lista):
    if i % 2 == 0:
        soma = soma + lista[i]
    i = i + 1
i = 0
while i < 5:
    if lista[i] > maior5:
        maior5 = lista[i]
    i = i + 1
print('Soma: ', soma)
print('O maior dos 5 primeiros: ', maior5)
print('O ultimo elemento: ', (lista[len(lista)-1]))
