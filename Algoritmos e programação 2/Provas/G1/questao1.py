lista = [[1, 2], [3, 4, 5], [10, 6, 7, 8, 9], [5, 4], [7]]

nova = []

print(lista)
for i in range(len(lista)):
     soma = sum(lista[i])
     nova.append(max(lista[i]))
     lista[i].append(soma)
nova.append(sum(nova))
lista.append(nova)
print(lista)


