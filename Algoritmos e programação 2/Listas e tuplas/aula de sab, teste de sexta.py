print('Excemplo dado na aula')
'''
lista1 = ['a', 'b', 'c']
lista2 = ['d', 'e']
print(lista1) #['a', 'b', 'c']
print(lista2)# ['d', 'e']
lista1.append(lista2)
print(lista1)#['a', 'b', 'c', ['d', 'e']]
print(lista2)#['d', 'e']
lista3 = ['f', 'g']
lista2.extend(lista3)
print(lista2)#['a', 'b', 'c', 'd', 'e']
print(lista3)#['f', 'g']
lista1.insert(2, 'x')
print(lista1) #['a', 'b', 'x', 'c', ['d', 'e']]
lista1[2] = 'y'
print(lista1)#['a', 'b', 'y', 'c', ['d', 'e']]
lista1.remove('b')
print(lista1)#['a', 'y', 'c', ['d', 'e']]
lista1.pop()
print(lista1)#['a', 'y', 'c']
x = lista1.pop()
print(x) #['a', 'y']
print(lista1) #['a', 'y', 'c']
y = lista1.pop(2)
print(y)#['a', 'y']
print(lista1)#['a', 'y', 'c']
lista1.pop(1)
print(lista1)#['a', 'c']
'''

print('Aula de sabado')
notas=[["eva","leo","bia"],[3.4,4.5,6.0],[7.0,3.0,6.5]]
lista=[]
lista1=[]
for i in range(len(notas)):
    media=(notas[1][i]+(notas[2][i]*2))/3
    lista.append(media)
    if media>=6:
        lista1.append("A")
    else:
        lista1.append("R")
notas.append(lista)
notas.append(lista1)
print(notas)

print('APPEND')
lista1 = ['a', 'b', 'c']
lista2 = ['e', 'f']
lista1.append(lista2)
lista1[3][1] = 'x' # lista1 recebe x / lista2 tambem recebe x, pois o endereço é atribuido
print(lista1)
print(lista2)

print('Insert')
lista1 = ['a', 'b', 'c',['d', 'e']]
lista1[3].insert(0, 'y')
lista1.insert(-1, 'x')
lista1[0] = 'k'
print(lista1)

print('remove')
l = [['a', 'b'],['a', 'd'],['x', 'a']]
for i in l:
     i.remove('a')
print(l)


print('pop')
l = ['a', 'b',' c']
print(l)
print(l.pop(1))
l.insert(0, 'z')
print(l)
if l.pop(1) == 'c':
     print('A lista tinha C')
print(l)


print('index')
l = ['a', 'b', 'c'] 
if l.index('a')==0:
     print('\'a\' é o primeiro valor da lista')

print('count')
l = ['a','b','a','c','a','d','a','a']
for i in range(l.count('a')):                  #count
     l.remove('a')
     print(l)

print('Sort e reverse')
l = ['x','a','c','y']
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print('---------------------------------------------------------------')
print('aula de sabado')

#questao doteste da turma de sexta

lista = [['A','B'],['X','Y'],['A'],['A','B','A']]
valor = 'A'
print(lista)

for sublista in lista:
    while valor in sublista:
        sublista.remove(valor)
    print(lista)
print()

# observar os indices


lista = ['osso', 'radar', ['asa', 'ovo']]
print(lista[2][0])
print(lista[2][0][1])
print()


lista = ['osso', 'radar', [['a','s','a'], ['o','v','o']]]
print(lista[:2])
for i in lista[:2]:
    print(i)
print()


lista = ['Parcilene', 'Fernandes', 'de', 'Brito']
print(lista[-1], end=', ')
ate = len(lista)-1
for i in lista[:ate]:
    print(i, end=' ')
print()
print()



lista = ['Parcilene', 'Fernandes', 'de', 'Brito']
print(lista[-1], end=', ')
for i in lista[:len(lista)-1]:
    print(i, end=' ')
print()
print()



#estudar com atenção
nomes = [['Fabiano','Fagundes'], ['Parcilene', 'Fernandes', 'de', 'Brito'],['Cristina', 'Filipakis']]

for i in nomes:
    print(i[-1], end=', ')
    for j in i[:-1]:
        print(j, end=' ')
    print()
print()


nomes = [['Fabiano','Fagundes'], ['Parcilene', 'Fernandes', 'de', 'Brito'],['Cristina', 'Filipakis']]
i = 0
while i < len(nomes):
    print(nomes[i][-1], end=',')
    j = 0
    while j < len(nomes[i])-1:
        print(nomes[i][j], end=' ')
        j += 1
    i += 1
    print()
print()





cpf = [111, 222, 333,44]
if cpf[0] % 2 == 0 and cpf[1] % 2 == 0 and cpf[2] % 2 == 0 and cpf[3] % 2 == 0:
    print('CPF válido!')
elif cpf[0] % 2 != 0 and cpf[1] % 2 != 0 and cpf[2] % 2 != 0 and cpf[3] % 2 != 0:
    print('CPF válido!')
else:
    print('CPF inválido!')
print()



cpfs = [[111, 222, 333,44],[110, 222, 334, 45],[111, 233, 333, 34]]
for cpf in cpfs:
    if cpf[0] % 2 == 0 and cpf[1] % 2 == 0 and cpf[2] % 2 == 0 and cpf[3] % 2 != 0:
        print('CPF válido!')
    elif cpf[0] % 2 != 0 and cpf[1] % 2 != 0 and cpf[2] % 2 != 0 and cpf[3] % 2 == 0:
        print('CPF válido!')
    else:
        print('CPF inválido!')
print()



tri =[[4, 2],[5, 10],[3, 6]]
print(tri)
for t in tri:
    a = (t[0] * t[1]) /2
    t.append(a)
print(tri)


print('-------------------------------------------------------------------')
print('Teste de sexta')

lista = [['A', 'B'],['X','Y'], ['A'],['A','B','A']]
valor = 'A'
print(lista)
for i in lista:
     while valor in i:
          i.remove(valor)
print(lista)
print()

lista = [['A', 'B'],['X','Y'], ['A'],['A','B','A']]

x = 'A'
print(lista)
for i in lista:
     for j in i:
          if j == x:
               i.remove(j)
print(lista)

print()
print('Teste de mesa')

lista1 = ['A','B','C','D']
lista2 = ['X','Y','Z']
lista3 = []
lista3.extend(lista2)
print(lista1)
print(lista2)
print(lista3)

lista1.insert(0,'M')
print(lista1)
print(lista2)
print(lista3)

lista1.append(lista2)
lista1[5][0]= 'K'
print(lista1)
print(lista2)
print(lista3)

lista3.append(lista1.pop())
print(lista1)
print(lista2)
print(lista3)

lista2.remove('Z')
print(lista1)
print(lista2)
print(lista3)

lista1.sort()
lista1.reverse()
lista3[3].reverse()
print(lista1)
print(lista2)
print(lista3)




