idade = int(input('Digite a idade: '))
peso = float(input('Digite o peso: '))
if idade > 12 and peso <= 60:
    print('30 Gotas!')
elif idade > 12 and peso > 60:
    print('40 Gotas!')
else:
    if peso <= 10:
        print('5 Gotas!')
    elif peso <= 20:
        print('10 Gotas!')
    elif peso <= 30:
        print('15 Gotas!')
    else:
        print('20 Gotas!')
