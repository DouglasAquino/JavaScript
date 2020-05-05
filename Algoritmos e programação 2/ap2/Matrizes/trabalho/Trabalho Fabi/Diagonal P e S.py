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
     print('Matriz: ')
     for i in range(len(matriz)):
          print(matriz[i])
else:
     print('Não é uma matriz quadrada!')
           
# Diagonal principal
print('Matriz')
matriz = [[10, 20, 30],
          [100, 200, 300],
          [50, 100, 150]]

for i in range(len(matriz)):
     print(matriz[i])

print('\n')
j = 0
print('Diagonal Principal:')
for i in matriz:
     print(i[j], end='  ')
     j += 1
print()
           
# Diagonal Secundaria

matriz = [[1, 2, 3],
          [4, 5, 6],
          [6, 7, 8]]
print('Matriz')
for i in range(len(matriz)):
     print(matriz[i])
print('\n')

print('Diagonal secundaria')
n = -1
for linha in matriz:
     print(linha[n], end=' ')
     n -= 1
 
