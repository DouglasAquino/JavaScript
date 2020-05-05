# Matriz Transposta
matriz = [[16, 68, 97],
          [21, 20, 19],
          [34, 15, 10]]
print('Matriz')
for i in range(len(matriz)):
     print(matriz[i])
print('------------------')
print('Matriz Transposta:')
mt = []
for i in range(len(matriz)):
     linha = []
     for j in range(len(matriz)):
          linha.append(matriz[j][i])
     mt.append(linha)
for i in range(len(mt)):
     print(mt[i])
