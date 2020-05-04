lista = []
for num in range(100, 19, -2):
    lista.append(num)
print(lista)
for i in range(len(lista)):
    if i % 2 == 0:
        print(lista[i])
