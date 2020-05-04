idade = int(input('Digite a idade: '))

if idade < 18:
    print('Não pode entrar!')
else:
    local = input('Digite o local escolhido: ')
    if local == 'camarote':
        print('R$150.00')
    else:
        print('R$100.00')
