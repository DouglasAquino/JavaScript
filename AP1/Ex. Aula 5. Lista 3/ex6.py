assiste = int(input('Quantidade que assistiram a apresentação: '))
sim = 0
nao = 0
cont = 0
while cont < assiste:
    gostou = input('Gostou da apresentação: ')
    if gostou == 'sim':
        sim = sim + 1

    else:
        nao = nao + 1
    cont = cont + 1
if sim > nao:
    print('A maioria gostou!')
elif nao > sim:
    print('A maioria não gostou!')
else:
    print('Empate!')
