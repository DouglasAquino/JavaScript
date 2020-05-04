lista = []
i = 0
while i < 10:
    lista.append(float(input('Numero: ')))
    i = i + 1
print(lista)
i = 0
while i < 10:
    if i < 5:
        lista[i] = 10
    else:
        lista[i] = lista[i] * 2
    i = i + 1
print(lista)
