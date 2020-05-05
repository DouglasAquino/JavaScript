lista1 = [] # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lista2 = [] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista3 = [] # [[9, 0], [8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]
lista4 = [] # [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]
lista5 = [] # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

for i in range(10):
     lista1.insert(0, i) 

for i in lista1:
     lista2.insert(0, i)

for i in lista2:
     lista3.append([i])

j = 0
for i in lista1:
     lista3[j].append(i)
     j += 1

for i in lista3:
     lista4.insert(0, i)

for i in lista4:
     a = i[0]
     i[0] = i[1]
     i[1] = a

for i in lista3:
     lista5.append(i[0] + i[1])

print(lista1[4]) # 5          
print(lista2[4]) # 4
print(lista3[4]) # [5, 4]
print(lista4[4]) # [4, 5]
print(lista5[4]) # 9
