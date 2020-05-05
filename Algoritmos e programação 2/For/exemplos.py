print('Um pouco mais de LISTAS (Na verdade, é a desculpa para falar do FOR)')
print('O for só funciona para estruturas em que você sabe quantas vezes haverá a repetição, tipo listas.')

lista=["a", 1, "x+y", 1+2]
for i in lista:
    print (i)
print('------------------------------------------')


print('FOR (com A função RANGE())')
for i in range(10):
    print(i)
#Testar no for:
#range(5,10)
#range(0,10,2)
#range(-10,-100,-30)
print('------------------------------------------')


print('FOR')
lista=["uva", "pera", "maça"]
for i in range(len(lista)):
    print (i, "-",lista[i])
print('------------------------------------------')


print('Enumerate')
lista=["uva", "pera", "maça"]
for indice, valor in enumerate(lista):
	print (indice, "-", valor)
print('------------------------------------------')


print('FOR em listas- CUIDADOS')
# LOOP
'''
lista=["1","2","3"]
for i in lista:
    lista.append(i)
    print(i)
'''
lista=["1","2","3"]

for i in lista:
    lista.insert(0,'a')
    print('i=',i)



print('------------------------------------------')
































