lista = [] # insere um numero na lista >0
num = int(input('numero:'))
while num >0:
    lista.append(num)
    num = int(input('numero:'))
#verificar se o numero existe na lista
numpesq = int(input('numero a pesquisar:'))
if numpesq in lista:
    print(numpesq, 'existe na lista!')
else:
    print(numpesq, ' nao existe na lista!')

        
