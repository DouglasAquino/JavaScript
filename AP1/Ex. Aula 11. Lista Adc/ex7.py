numeros = [20, -7, 8, -5, 4, -6, 3, 20, -2, -8, 9, 20, 15, -5, 8]
novaLista = []
for i in range(len(numeros)):
    if i < 5:
        novaLista.append(numeros[i] * 2)
    else:
        novaLista.append(numeros[i])
print(numeros)
print(novaLista)
