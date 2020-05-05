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
               
