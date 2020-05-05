# Matriz quadrada

matriz = []
linhas = int(input('Quantas linhas? '))
colunas = int(input('Quantas colunas? '))
if linhas == colunas:
     print('---------------')
     print('Matriz Quadrada')
     print('---------------')
     for c1 in range(0, colunas):
         linha = []
         for c2 in range(0, linhas):
             n = int(input('Número Linha[{0}] Coluna[{1}]: '.format(c1 + 1,c2 + 1)))
             linha.append(n)
         matriz.append(linha)
     print('------------')
     print('Matriz: ')
     for i in range(len(matriz)):
          print(matriz[i])
else:
     print('---------------------------')
     print('Não é uma matriz quadrada!')
     print('---------------------------')
