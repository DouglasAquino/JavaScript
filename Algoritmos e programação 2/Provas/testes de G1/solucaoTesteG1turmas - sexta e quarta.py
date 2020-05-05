
lista = [['X','B','A','A'],['X','A'],['D','K','Z'],['A']]



# Teste de sexta
'''

valor = 'A'

print('Lista antes:', lista)

for i in lista:
    
    while valor in i:
        i.remove(valor)

print ('Lista depois', lista)
'''

# Teste de quarta - alternativa 1
'''
print('Lista antes:', lista)

valor = 'A'


for i in lista:

    while valor in i:
        posicao = i.index(valor)
        i[posicao] = lista[0][0]

print ('Lista depois', lista)
'''
# Teste de quarta - alternativa 2

print('Lista antes:', lista)

valor = 'A'

sub=lista[0][0]

for i in lista:
    for x in range(len(i)):
        if i[x] == 'A':
            i[x] = sub

print('Lista depois: ',lista)
        
        
