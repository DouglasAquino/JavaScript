# Matriz Simetrica
# Simetrica
print('Matriz')
matriz = [[3, 5, 6],
          [5, 2, 4],
          [6, 4, 8]]

for i in range(len(matriz)):
     print(matriz[i])
     
simetrica = True
i = 0
while simetrica and i < len(matriz):
     j = 0
     while simetrica and j < i:
          if matriz[i][j] != matriz[j][i]:
               simetrica = False
          j += 1
     i += 1
if simetrica:
     print('A matriz é simetrica!')
else:
     print('A matriz não é simetrica!')
print('-----------------------')

# Nao simetrica
print('Matriz')
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

for i in range(len(matriz1)):
     print(matriz1[i])
     
simetrica = True
i = 0
while simetrica and i < len(matriz):
     j = 0
     while simetrica and j < i:
          if matriz1[i][j] != matriz1[j][i]:
               simetrica = False
          j += 1
     i += 1
if simetrica:
     print('A matriz  é simetrica!')
else:
     print('A matriz não é simetrica!')
