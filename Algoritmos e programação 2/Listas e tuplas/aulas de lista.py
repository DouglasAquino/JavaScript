lista = ['A', 5, True, 'X']
print(lista)
print(lista[0])
for i in lista:
     print(i)
for i in range(len(lista)):
     print(i, lista[i])
for i, j in enumerate(lista):
     print(i, j)
print()

print('-------------------------------------------------------------------')

lista1 = ['A', ['B', 'C'], 'D']
print(lista1)
print(lista1[1])
print(lista1[1][0])
print()

print('---------------------------------------------------------------------')

lista2 = [['A', 'B'], ['C', 'D'],['E', 'F']]
print(lista2)
for i in lista2:
     print(i)
for i, j in lista2:
     print(i, j)
for i in lista2:
     print(i)
     for j in i:
          print(j, end=' ')
     print()
print()

print('----------------------------------------------------------------------')

m = [[0, 1, 2], [3, 4, 5],[6, 7, 0]]
print(m)
cont = 0
for i in m:
     for j in i:
          cont += j
if cont == 0:
     print('Nula!')
else:
     print('Não nula!')
print()

m1 = [[0, 0, 0],[2, 3, 4], [5, 6, 7]]
print(m1)
cont = 0
for i in m1:
     for j in i:
          if j == 0:
               cont += 1
if cont == 9:
     print('Nula!')
else:
     print('Não nula!')
print()

m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(m2)
nula = True
for i in m2:
     for j in i:
          if j != 0:
               nula = False
if nula:
     print('Nula')
else:
     print('Não nula')

print()
print('-------------------------------------------------------------------------')

m = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
if len(m) == len(m[0]):
     print('È uma matriz quadrada!')
     linha = int(input('Que linha voce quer imprimir: '))
     print('Linha: ', m[linha-1])
     coluna = int(input('Que coluna voce quer imprimir: '))
     for i in range(len(m)):
          print(m[i][coluna-1])
     posilinha = int(input('Que linha voce deseja alterar: '))
     posicolu = int(input('Que coluna voce deseja alterar: '))
     alterar = int(input('Novo valor para a alteração: '))
     m[posilinha-1][posicolu-1] = alterar
     print('Nova matriz: ')
     for i in m:
          print(i)
     inlinha = int(input('Digite a linha: '))
     incolu = int(input('Digite a coluna: '))
     print(m[inlinha-1][incolu-1])












               
          
