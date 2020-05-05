# 1
print('Questao 1')
lista = ['doce','carne','arroz', 'erva', 'banana']
print(lista)
lista_ordenada = sorted(lista, key=len)

print(lista_ordenada)
print()

# 2
print('Questao 2')
lista = ['doce','carne','arroz', 'erva', 'banana']
print(lista)
lista.sort()
print(lista)
print()

# 3
print('Questao 3')
lista1 = [1, 2, 3]
lista2 = [5, 6, 7, 8, 9, 0]
lista3 = []
i=0
j=0
while i<len(lista1) and j <len(lista2):
     lista3.append(lista1[i])
     lista3.append(lista2[i])
     i+=1
     j+=1
     
if len(lista1)>len(lista2):
     lista3.extend(lista1[i:])
else:
     lista3.extend(lista2[i:])

print(lista3)
print()

# 1
print('Questao 1')
lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
i = 1
while i in range(len(lista)):
     if i % 2 == 0:
          print(lista[i], end=" ")
     i += 1
print()
print()

# 2
print('Questao 2')
lista = ['a', 'e', 'c', 'd', 'b']
lista1 = lista
print(lista)
lista1.sort()
print(lista1)
print()

# 3
print('Questao 3')
lista_par = []
lista_impar = []

for i in range(10):
     num = int(input('Digite um número: '))
     if num % 2 == 0:
          lista_par.append(num)
     else:
          lista_impar.append(num)
print(lista_par)
print(lista_impar)
print()

# 4
print('Questao 4')
lista = [[1, 2, 3, 4, 5, 6],[10, 11, 12],[12, 22, 34]]
for i in lista:
    listamaior=[]
    listamaior.append(max(i))
    print(max(i), end=' ')
print()
print(max(listamaior))
print()

# 5
print('Questao 5')
lista = [[1, 2, 3],[5, 5, 5],[10, 2]]
print(lista)
for i in range(len(lista)):
     soma = sum(lista[i])
     lista[i].append(soma/len(lista[i]))
print(lista)
soma = 0
s = 0
for i in range(len(lista)):
     soma += sum(lista[i])
     s += len(lista[i])
lista.append(soma/s)
print(lista)
print()

# 6
print('Questao 6')
lista = [[2.5, 3.4, 6.7, 1.2],[1.1, 1.2, 1.3, 11.4],[2.1, 3.1, 4.1, 12.1],[5.5, 5.5, 5.5, 7.5]]
print(lista)
soma = 0
maior = 0
for i in range(len(lista)):
     soma += lista[i][0]
     for j in range(len(lista)):
          lista[i][1] = 0
          if lista[i][j] > maior:
               maior = lista[i][j]
print(lista)
for i in range(len(lista)):
     lista[i][2] = maior
     for j in range(len(lista)):
          if lista[i][3] > 10:
               lista[i][3] = 10
          if lista[i][3] < 10:
               lista[i][3] = 0

print(lista)
print('Soma de todos primeiros elementos: ', soma)














 
