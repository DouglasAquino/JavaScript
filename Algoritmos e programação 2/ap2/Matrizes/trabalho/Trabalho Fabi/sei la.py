# Matriz quadrada
matriz = []
linhas = int(input('Quantas linhas? '))
colunas = int(input('Quantas colunas? '))
if linhas == colunas:
     for c1 in range(0, colunas):
         linha = []
         for c2 in range(0, linhas):
             n = int(input('Número Linha[{0}] Coluna[{1}]: '.format(c1 + 1,c2 + 1)))
             linha.append(n)
         matriz.append(linha)
     print('-----------------')
     print('Matriz Quadrada: ')
     for i in range(len(matriz)):
          print(matriz[i])
else:
     print('Não é uma matriz quadrada!')
print('=====================================================================')

# Diagonal principal
print('Matriz')
matriz = [[10, 20, 30],
          [80, 23, 34],
          [50, 19, 15]]
for i in range(len(matriz)):
     print(matriz[i])
print('-----------------------')
j = 0
print('Diagonal Principal:')
for i in matriz:
     print(i[j], end='  ')
     j += 1
print()
print('------------------------')

# Diagonal Secundaria
print('Diagonal secundaria')
n = -1
for linha in matriz:
     print(linha[n], end=' ')
     n -= 1
print()
print('=====================================================================')

# Matriz Triangular
matriz = [[5, 0, 0],
          [9, 9, 0],
          [3, 6, 9]]
print('Matriz')
for i in range(len(matriz)):
     print(matriz[i]) # Imprime a matriz
     
superior = 'verdade'
inferior = 'verdade'
nao = 'falso'
for i in range(len(matriz)):
     for j in range(len(matriz)):
          if i < j and matriz[i][j] != 0: # Confere se a matriz é T. superior
               superior = 'falso'
          if i > j and matriz[i][j] != 0: # Confere se a matriz é T. inferior
               inferior = 'falso'
          if i == j and matriz[i][j] == 0: # Confere se é uma matriz T.
               nao = 'verdade'
if nao == 'verdade':
     print('Não é uma matriz Triangular!')
else:
     if superior == 'verdade':
          print('Matriz Triangular superior!')
     if inferior == 'verdade':
          print('Matriz Triangular inferior!')

          
print('=====================================================================')

# Matriz Diagonal
matriz = [[9, 0, 0],
          [0, 5, 0],
          [0, 0, 8]]
print('Matriz')
for i in range(len(matriz)):
     print(matriz[i])
teste = True
for i in range(len(matriz)):
     for j in range(len(matriz)):
          if i == j and matriz[i][j] < 1:
               teste = False
          elif i != j and matriz[i][j] != 0:
               teste = False
if teste:
     print('É uma matriz Diagonal!')
else:
     print('Não é uma matriz Diagonal!')
               
print('=====================================================================')

# Matriz Identidade
matriz = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]
print('Matriz')
for i in range(len(matriz)):
     print(matriz[i])
teste = True
for i in range(len(matriz)):
     for j in range(len(matriz)):
          if i == j and matriz[i][j] != 1:
               teste = False
          elif i != j and matriz[i][j] != 0:
               teste = False
if teste:
     print('É uma matriz identidade!')
else:
     print('Não é uma matriz identidade!')
               

print('=====================================================================')

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
if soma == 0:
     print('A Matriz é Nula!')
else:
     print('A Matriz não é Nula!')

print('=====================================================================')

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

print('=====================================================================')

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

print('=====================================================================')
           
# Matriz Oposta
print('Matriz:')
matrizOposta = [[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]]

for i in range(len(matrizOposta)):
     print(matrizOposta[i])
print('-----------------')
print('Matriz Oposta:')
for i in range(len(matrizOposta)):
     for j in range(len(matrizOposta)):
          matrizOposta[i][j] = matrizOposta[i][j] * -1
for i in range(len(matrizOposta)):
     print(matrizOposta[i])

     

               
