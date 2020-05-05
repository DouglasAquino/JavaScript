print('endereços')
x = 5
print(x)
print(id(x))
x = 7
print(x)
print(id(x))
z = 5
print(z)
print(id(z))
print()

lista = [5, 7, 'A', 7]
print(id(lista))
print(id(lista[0]))
print(lista[1])
print(lista[3])
print()
lista2 = [0, 1, 2]
print(id(lista2))
print()
lista3 = [7, 7, 'A', '7']
print(lista)
print(id(lista))
print(lista3)
print(id(lista3))
print()
lista3[1]='ABC'
print(lista3)
print(id(lista3))
print()
lista4 = lista
lista4[0] = 100
print(lista)
print(lista4)
print(id(lista))
print(id(lista4))
print()
print('----------------------------------------------------------------------')

a = ''
if a:
     print(a)
b = 0
if b:
     print(b)
c = []
if c:
     print(c)
d = None
if d:
     print(d)
e = False
if e:
     print(e)
print()

print('-----------------------------------------------------------------------')
print('Falso ou verdadeiro:')
t1 = True
t2 = True
f1 = False
f2 = False
print(not t1)
if t1 and t2:
     print('Entrou 1')
if t1 and t2 and f1:
     print('Entrou 2')
if t1 and(t2 and f1):
     print('Entrou 3')
if t1 and t2 or f1:
     print('Entrou 4')
if t1 and(t2 or f1):
     print('Entrou 5')
if (t1 and t2) or f1:
     print('Entrou 6')
if t1 or t2 and f1:
     print('Entrou 7')
if t1 and f1 or t2:
     print('Entrou 8')
if t1 and f1 or f2:
     print('Entrou 9')
if t1 or f1 and f2:
     print('Entrou 10')
if (t1 or f1) and f2:
     print('Entrou 11')
print()

print('---------------------------------------------------------------------------')

a = 10
b = 10
c = 20
if a and b == 10:
     print('Entrou A')
if a and c == 10:
     print('Entrou B')
if a and c == 20:
     print('Entrou C')
if c and a == 10:
     print('Entrou D')
     

























