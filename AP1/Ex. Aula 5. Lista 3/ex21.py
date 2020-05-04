qt = int(input('Quantidade de funcionarios: '))
mediaSal = 0
cont = 0
menorSal = 100000
while cont < qt:
    nome = input('Nome do funcionario: ')
    qtPecas = int(input('Quantidade de peças: '))
    salario = 1000 + qtPecas * 1.50
    if salario < 1500:
        print('Nome: ', nome, '--', 'Categoria A!', '--', 'Salario R$', salario)
    elif salario < 2000:
        print('Nome: ', nome, '--', 'Categoria B!', '--', 'Salario R$', salario)
    elif salario < 2500:
        print('Nome: ', nome, '--', 'Categoria C!', '--', 'Salario R$', salario)
    else:
        print('Nome: ', nome, '--', 'Categoria D!', '--', 'Salario R$', salario)
    if salario < menorSal:
        menorSal = salario
    mediaSal = mediaSal + salario
    cont = cont + 1
print('Media salarial R$', mediaSal/qt)
print('Menor Salario: ', menorSal)
