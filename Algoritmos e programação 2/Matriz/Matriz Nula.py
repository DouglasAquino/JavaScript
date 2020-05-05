# Matriz Nula
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma = 0
print('Matriz')
for i in range(len(matriz)):
     for j in range(len(matriz)):
          soma += matriz[i][j]
for i in range(len(matriz)):
     print(matriz[i])
print('------------')
if soma == 0:
     print('Matriz Nula!')
else:
     print('Matriz não Nula!')
