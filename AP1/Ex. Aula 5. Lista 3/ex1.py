cont = 0
mulheres = 0
homens = 0
while cont < 10:
    cont = cont + 1
    sexo = input('Sexo: ')
    if sexo == 'f':
        mulheres = mulheres + 1
    else:
        homens = homens + 1
print('Quantidade de Mulheres: ', mulheres)
print('Quantidade de Homens: ', homens)
