lista = []
i = 0
while i < 10:
    lista.append(int(input('Numero: ')))
    i = i + 1
print(lista)
i = 0
while i < len(lista):
    if i % 2 == 0:
        lista.pop(i)
    i = i + 1
print(lista)
