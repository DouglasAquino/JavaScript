lista = []
listaA = []
listaB = []
i = 0
while i < 20:
    num = int(input('Numeros: '))
    lista.append(num)
    if i % 2 == 0:
        listaA.append(lista[i])
    else:
        listaB.append(lista[i])
    i = i + 1
print(lista)
print(listaA)
print(listaB)
