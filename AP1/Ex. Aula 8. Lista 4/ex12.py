lista = []
i = 0
while i < 10:
    lista.append(int(input('Numeros: ')))
    i = i + 1
print(lista)
aux = lista[9]
lista[9] = lista[0]
lista[0] = aux
print(lista)
