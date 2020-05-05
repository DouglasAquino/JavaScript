lista = [['Pão', 1.1, 2],
         ['Cuscuz', 1.2, 2],
         ['Salshicha', 2.3, 5]]

for i in range(len(lista)):
    lista[i].append(lista[i][1] * lista[i][2])

for i in range(len(lista)):
    if lista[i][3] >= 5:
        lista[i].append('Caro')
    else:
        lista[i].append('Barato')
    
print(lista)
