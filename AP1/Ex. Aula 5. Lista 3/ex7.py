salMim = float(input('Salario minimo R$'))
cont = 0
mediaA = 0
maiorSal = 0
contA = 0
while cont <100:
    nome = input('Nome do Funcionario: ')
    qtPecas = int(input('Quantidade de peças: '))
    salario = salMim + qtPecas * 1.5
    if salario > maiorSal:
        maiorSal = salario
    if qtPecas < 5000:
        mediaA = mediaA + salario
        contA = contA + 1
        print('Nome: ', nome, '\nCategoria A.', '\nSalário R$', salario)
    elif qtPecas <= 10000:
        print('Nome: ', nome, '\nCategoria B.', '\nSalario R$', salario)
    else:
        print('Nome: ', nome, '\nCategoria C.', '\nSalario R$', salario)
    cont = cont + 1
if contA > 0:
    print('Media: ', mediaA / contA)
print('Maior salario R$', maiorSal)
