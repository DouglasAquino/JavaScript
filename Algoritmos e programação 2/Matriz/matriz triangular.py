# Matriz Triangular

matriz = [[5, 0, 0],
          [9, 9, 0],
          [5, 0, 9]]
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

          
