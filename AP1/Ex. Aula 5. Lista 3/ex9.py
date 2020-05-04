branco = 0
tinto = 0
rose = 0
cont = 0
tipo = input('Tipo de vinho: ')
while tipo == 'branco' or tipo == 'rose' or tipo == 'tinto':
    if tipo == 'branco':
        branco = branco + 1
    elif tipo == 'tinto':
        tinto = tinto + 1
    elif tipo == 'rose':
        rose = rose + 1
    tipo = input('Tipo de vinho: ')
    cont = cont + 1

if tipo != 'branco' or tipo != 'rose' or tipo != 'tinto':
    print('Opção invalida!')
    
if cont != 0:
    print('Percentual de Vinhos Brancos: ', (branco * 100) / cont)
    print('Percentual de Vinho Tinto: ', (tinto * 100) / cont)
    print('Percentual de Vinho Rose: ', (rose * 100) / cont)
    

