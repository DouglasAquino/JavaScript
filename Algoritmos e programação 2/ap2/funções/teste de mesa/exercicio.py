def testeA(texto1, texto2):
    lista = [texto1, texto2] # ['def', 'abc']
    lista.sort() # ['abc', 'def']
    return lista[0]

def testeB(texto1, texto2):
    lista = [texto1, texto2] # [['abc', 'def']
                             #['xyz', klm']]
    lista[0:1] = [lista[0].upper(),lista[1].upper()] #['ABC', 'DEF', 'def']
                                                     #['XYZ', 'KLM', 'klm']
    return lista

def testeC(texto1,texto2): # 'abc', 'def'
    texto1.upper() # 'abc'
    texto2.upper() # 'def'
    return texto1,texto2

string1 = 'abc'
string2 = 'def'

x = testeA(string2, string1) # abc
y = testeB(string1, string2) # ['ABC', 'DEF', 'def']
z = testeC(string1, string2) # ('abc', 'def')
k = testeB('xyz','klm') # ['XYZ', 'KLM', 'klm']

print('x[0]=',x[0]) # x[0] = a
print('y[0][1]=',y[0][1]) # y[0][1] = B
print('y[1][1]=',y[1][1]) # y[1][1] = E
print('y[2][1]=',y[2][1]) # y[2][1] = e
print('z[0][1]=',z[0][1]) # z[0][1]= b
print(z) # ('abc', 'def')
print(y) # ['ABC', 'DEF', 'def']
print(x) # abc
#z.append(x)
#print(z) # 'tuple' object has no attribute 'append'
y.append(x)
print(y) # ['ABC', 'DEF', 'def', 'abc']
#x.append(y)
#print(x) # AttributeError: 'str' object has no attribute 'append'
print(testeA(testeB(y[0],y[1])[0],\
      testeC(z[0],x)[0])) # ABC

k[2].upper()
print(k[2]) # klm

print(k[2].upper()) # KLM

if k[2].upper()[1]==k[2][1].upper():
    print('São iguais') # Sao iguais
else:
    print('Não são iguais')






