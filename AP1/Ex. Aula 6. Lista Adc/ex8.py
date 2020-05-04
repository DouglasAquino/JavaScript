ingresso = float(input('Valor do ingresso: '))
cont = 0
meia = 0
metade = 100/2
while cont < 100:
    sexo = input('Sexo: ')
    idade = int(input('Idade: '))
    pagamento = input('Pagou meia entrada: ')
    if pagamento == 'sim':
        meia = meia + 1
        print('Pagou R$', ingresso / 2)
    else:
        print('Pagou R$', ingresso)
    cont = cont + i
if meia == metade:
    print('Pelo menos a metade pagou meia entrada!')
elif meia < metade:
    print('Menos da metade pagou nmeia entrada!')
else:
    print('Mais da metade pagou meia entrada!')
    
