listaQt = []
listaVal = []
listaTotal = []
i = 0
maior = 0
qtMaior = 0
qt = int(input('Quantidade: '))
while qt >= 0:
    listaQt.append(qt)
    listaVal.append(float(input('Valor: ')))
    listaTotal.append(listaQt[i] * listaVal[i])
    qt = int(input('Quantidade: '))
    i = i + 1
print('Valores totais R$: ', listaTotal)
i = 0
while i < len(listaQt):
    if listaQt[i] < 50:
        print('Codigo {} tem {} em estoque.'.format(i, listaQt[i]))
        print('Precisa de reposição!')
    if maior < listaVal[i]:
        maior = listaVal[i]
    i = i + 1
i = 0
while i < len(listaVal):
    if listaVal[i] == maior:
        qtMaior = qtMaior + 1
    i = i + 1
print('Maior: ', maior)
print('Quantidade igual ao maior: ', qtMaior)
