lista = []
i = 0
lista.append(int(input('Numero: ')))
while lista[i] < 30000:
    lista.append(lista[i] + 10)
    i = i + 1
print(lista)
