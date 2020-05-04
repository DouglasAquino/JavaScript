lista = []
positivos = []
negativos = []
i = 0
while i < 20:
    num = int(input('Numero: '))
    lista.append(num)
    if num >= 0:
        positivos.append(num)
    else:
        negativos.append(num)
    i = i + 1
print(lista)
print(positivos)
print(negativos)
